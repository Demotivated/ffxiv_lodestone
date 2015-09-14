from django.http import JsonResponse, HttpResponseServerError
import logging

import requests
from lxml import html

from .models import Character
from .exceptions import ParsingException
from .constants import USER_AGENT


def scrape_by_id(request, lodestone_id):
    try:
        logging.debug('Attempting to parse id {}'.format(lodestone_id))

        try:
            headers = {'User-Agent': USER_AGENT}
            uri = 'http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(lodestone_id)
            page = requests.get(uri, headers=headers)
            assert page.status_code == 200
        except AssertionError:
            raise ParsingException('Can\'t contact Lodestone')

        try:
            char = Character()
            tree = html.fromstring(page.text)

            char.lodestone_id = lodestone_id
            char.name = tree.xpath('//title/text()')[0].split('|')[0].strip()
            char.free_company = tree.xpath('//dd[@class="txt_name"]/a[contains(@href, "")]/text()')[0]
            char.server = tree.xpath('//h2//span/text()')[0].strip()[1:-1]

            info = tree.xpath('//dd[@class="txt_name"]/text()')
            _, _, char.city_state, char.grand_company = info

            info = tree.xpath('//div[@class="chara_profile_title"]')
            species, _, _ = info[0].text.split('/')
            char.species = species.strip()

            def lvl_from_index(index):
                char = class_list[index]
                if char == '-':
                    return 0
                else:
                    return int(char)

            class_list = tree.xpath('//td/text()')
            char.lvl_gladiator = lvl_from_index(0*3+1)
            char.lvl_pugilist = lvl_from_index(1*3+1)
            char.lvl_marauder = lvl_from_index(2*3+1)
            char.lvl_lancer = lvl_from_index(3*3+1)
            char.lvl_archer = lvl_from_index(4*3+1)
            char.lvl_rogue = lvl_from_index(5*3+1)
            char.lvl_conjurer = lvl_from_index(6*3+1)
            char.lvl_thaumaturge = lvl_from_index(7*3+1)
            char.lvl_arcanist = lvl_from_index(8*3+1)

            char.lvl_dark_night = lvl_from_index(9*3+1)
            char.lvl_machinist = lvl_from_index(10*3+1)
            char.lvl_astrologian = lvl_from_index(11*3+1)

            char.lvl_carpenter = lvl_from_index(12*3+1)
            char.lvl_blacksmith = lvl_from_index(13*3+1)
            char.lvl_armorer = lvl_from_index(14*3+1)
            char.lvl_goldsmith = lvl_from_index(15*3+1)
            char.lvl_leatherworker = lvl_from_index(16*3+1)
            char.lvl_weaver = lvl_from_index(17*3+1)
            char.lvl_alchemist = lvl_from_index(18*3+1)
            char.lvl_culinarian = lvl_from_index(19*3+1)
            char.lvl_miner = lvl_from_index(20*3+1)
            char.lvl_botanist = lvl_from_index(21*3+1)
            char.lvl_fisher = lvl_from_index(22*3+1)

            char.save()
        except (IndexError, ValueError):
            raise ParsingException('Unable to parse id {} from lodestone'.format(lodestone_id))

    except ParsingException as e:
        return HttpResponseServerError(e.message)

    return JsonResponse(char.as_dict())
