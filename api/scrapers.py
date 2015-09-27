from django.core.exceptions import ObjectDoesNotExist
import threading

import requests
from lxml import html

from .models import *
from .exceptions import ParsingException
from .constants import USER_AGENT, JOB_IDS


def scrape_character_by_id(lodestone_id):
    
    logging.debug('Attempting to parse character id {}'.format(lodestone_id))

    try:
        headers = {'User-Agent': USER_AGENT}
        uri = 'http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(lodestone_id)
        page = requests.get(uri, headers=headers)
        assert page.status_code == 200

    except AssertionError:
        raise ParsingException('Invalid response from Lodestone')

    try:
        # Populate Character
        char = Character()
        tree = html.fromstring(page.text)

        char.lodestone_id = lodestone_id
        char.name = tree.xpath('//title/text()')[0].split('|')[0].strip()
        char.free_company = tree.xpath('//dd[@class="txt_name"]/a[contains(@href, "")]/text()')[0]
        char.server = tree.xpath('//h2//span/text()')[0].strip()[1:-1]

        info = tree.xpath('//dd[@class="txt_name"]/text()')
        _, _, char.city_state, grand_company = info
        char.grand_company_name, char.grand_company_rank = grand_company.split('/')

        info = tree.xpath('//div[@class="chara_profile_title"]')
        species, _, _ = info[0].text.split('/')
        char.species = species.strip()
        char.save()

        class_list_from_html = tree.xpath('//td/text()')

        def level_from_index(index):
            level = class_list_from_html[index*3+1]

            def parse_level(html_level):
                if html_level == '-':
                    return 0
                else:
                    return int(html_level)
            return parse_level(level)

        # Populate classes
        char.lvl_gladiator = level_from_index(0)
        char.lvl_pugilist = level_from_index(1)
        char.lvl_marauder = level_from_index(2)
        char.lvl_lancer = level_from_index(3)
        char.lvl_archer = level_from_index(4)
        char.lvl_rogue = level_from_index(5)
        char.lvl_conjurer = level_from_index(6)
        char.lvl_thaumaturge = level_from_index(7)
        char.lvl_arcanist = level_from_index(8)

        char.lvl_darknight = level_from_index(9)
        char.lvl_machinist = level_from_index(10)
        char.lvl_astrologian = level_from_index(11)

        char.lvl_carpenter = level_from_index(12)
        char.lvl_blacksmith = level_from_index(13)
        char.lvl_armorer = level_from_index(14)
        char.lvl_goldsmith = level_from_index(15)
        char.lvl_leatherworker = level_from_index(16)
        char.lvl_weaver = level_from_index(17)
        char.lvl_alchemist = level_from_index(18)
        char.lvl_culinarian = level_from_index(19)

        char.lvl_miner = level_from_index(20)
        char.lvl_botanist = level_from_index(21)
        char.lvl_fisher = level_from_index(22)

        # Find current job
        job_images = tree.xpath('//div[@id="class_info"]/div[@class="ic_class_wh24_box"]/img')
        job_image_id = job_images[0].attrib['src'].split('?')[1]
        job_id = JOB_IDS[job_image_id].name

        job, _ = char.job_set.get_or_create(
            job=job_id
        )

        # Populate items
        html_item_list = tree.xpath('//div[@class="item_detail_box"]/div/div/div/div/a')
        item_ids = []
        for item_id in html_item_list:
            item_ids.append(item_id.attrib['href'].split('/')[5])

        # Grab items from database / grab in parallel
        item_threads = []
        for item_id in item_ids:
            try:
                job.items.add(Item.objects.get(lodestone_id=item_id))
            except ObjectDoesNotExist:
                thread = ItemThread(item_id)
                thread.start()
                item_threads.append(thread)
        for thread in item_threads:
            job.items.add(thread.join())

        job.save()

    except (IndexError, ValueError):
        raise ParsingException('Unable to parse id {} from lodestone'.format(lodestone_id))

    return char


class ItemThread(threading.Thread):

    def __init__(self, item_id):
        threading.Thread.__init__(self)
        self.item_id = item_id
        self._item = None

    def run(self):
        self._item = scrape_item_by_id(self.item_id)

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._item


def scrape_item_by_id(lodestone_id):

    logging.debug('Attempting to parse items from id {}'.format(lodestone_id))

    try:
        headers = {'User-Agent': USER_AGENT}
        uri = 'http://na.finalfantasyxiv.com/lodestone/playguide/db/item/{}/'.format(lodestone_id)
        page = requests.get(uri, headers=headers)
        assert page.status_code == 200

    except AssertionError:
        raise ParsingException('Invalid response from Lodestone')

    try:
        tree = html.fromstring(page.text)

        item, _ = Item.objects.get_or_create(lodestone_id=lodestone_id)
        item.name = tree.xpath('//title/text()')[0].split('|')[0].replace('Eorzea Database:', '').strip()
        item.save()

    except (IndexError, ValueError):
        raise ParsingException('Unable to parse item id {} from lodestone'.format(lodestone_id))

    return item
