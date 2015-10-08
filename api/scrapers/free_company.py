from django.core.exceptions import ObjectDoesNotExist

from api.models import FreeCompany, Character
from api.scrapers.character import CharacterThread, scrape_character_by_id
from api.constants import USER_AGENT
from api.exceptions import ParsingException

import requests
from lxml import html

import logging
import datetime
import re


def scrape_free_company_by_id(lodestone_id):
    logging.debug('Attempting to parse free company from id {}'.format(lodestone_id))

    try:
        headers = {'User-Agent': USER_AGENT}
        uri = 'http://na.finalfantasyxiv.com/lodestone/freecompany/{}/'.format(lodestone_id)
        page = requests.get(uri, headers=headers)
        assert page.status_code == 200

    except AssertionError:
        raise ParsingException('Invalid response from Lodestone')

    try:
        tree = html.fromstring(page.text)

        updated_values = {}

        _, name, server = \
            tree.xpath('//div[@class="crest_id centering_h"]/span/text()')
        updated_values['name'] = name
        updated_values['server'] = server[1:-1]
        updated_values['tag'] = tree.xpath('//td[@class="vm"]/text()')[0][1:-1]

        formed_js = str(tree.xpath('//td/script/text()')[0])
        updated_regex = re.search(r'ldst_strftime\(([0-9]+),', formed_js)
        updated_values['formed'] = datetime.datetime.fromtimestamp(int(updated_regex.group(1)))

        updated_values['rank'] = int(tree.xpath('//tr[@class="rank"]/td/text()')[0].strip())

        weekly_rank, monthly_rank, _ = tree.xpath('//tr[5]/td/text()')
        updated_values['weekly_rank'] = int(re.search(r'Rank: ([0-9]+) ', weekly_rank).group(1))
        updated_values['monthly_rank'] = int(re.search(r'Rank: ([0-9]+) ', monthly_rank).group(1))

        updated_values['slogan'] = tree.xpath('//tr[6]/td/text()')[0]

        fc, _ = FreeCompany.objects.update_or_create(lodestone_id=lodestone_id, defaults=updated_values)

        total_members = int(tree.xpath('//tr[3]/td/text()')[0])
        page_num = 1

    except (IndexError, ValueError):
        raise ParsingException('Unable to parse free company id {} from lodestone'.format(lodestone_id), exc_info=True)

    while total_members > 0:
        total_members -= 50
        page_num += 1

        try:
            headers = {'User-Agent': USER_AGENT}
            uri = 'http://na.finalfantasyxiv.com/lodestone/freecompany/{lodestone_id}/member/?page={page_num}'.format(
                lodestone_id=lodestone_id,
                page_num=page_num)
            page = requests.get(uri, headers=headers)
            assert page.status_code == 200

        except AssertionError:
            raise ParsingException('Invalid response from Lodestone')

        try:
            tree = html.fromstring(page.text)

            character_ids = map(
                lambda x: x.attrib['href'].split('/')[3],
                tree.xpath('//div[@class="name_box"]/a'))

            for character_id in character_ids:
                if character_id == '8774791':
                    fc.members.add(scrape_character_by_id(character_id))

            # Grab items from database / grab in parallel
            # character_threads = []
            # for character_id in character_ids:
            #     try:
            #         fc.members.add(Character.objects.get(lodestone_id=lodestone_id))
            #     except ObjectDoesNotExist:
            #         thread = CharacterThread(character_id)
            #         thread.start()
            #         character_threads.append(thread)
            # for thread in character_threads:
            #     fc.members.add(thread.join())

        except (IndexError, ValueError):
            raise ParsingException('Unable to parse free company id {} from lodestone'.format(lodestone_id),
                                   exc_info=True)

        fc.save()

    return fc
