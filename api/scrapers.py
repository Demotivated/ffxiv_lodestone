import logging

import requests
from lxml import html

from .models import *
from .exceptions import ParsingException
from .constants import USER_AGENT


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

        char.gladiator = Gladiator(
            level=level_from_index(0))
        char.pugilist = Pugilist(
            level=level_from_index(1))
        char.marauder = Marauder(
            level=level_from_index(2))
        char.lancer = Lancer(
            level=level_from_index(3))
        char.archer = Archer(
            level=level_from_index(4))
        char.rogue = Rogue(
            level=level_from_index(5))
        char.conjurer = Conjurer(
            level=level_from_index(6))
        char.thaumaturge = Thaumaturge(
            level=level_from_index(7))
        char.arcanist = Arcanist(
            level=level_from_index(8))

        char.darknight = DarkNight(
            level=level_from_index(9))
        char.machinist = Machinist(
            level=level_from_index(10))
        char.astrologian = Astrologian(
            level=level_from_index(11))

        char.carpenter = Carpenter(
            level=level_from_index(12))
        char.blacksmith = Blacksmith(
            level=level_from_index(13))
        char.armorer = Armorer(
            level=level_from_index(14))
        char.goldsmith = Goldsmith(
            level=level_from_index(15))
        char.leatherworker = Leatherworker(
            level=level_from_index(16))
        char.weaver = Weaver(
            level=level_from_index(17))
        char.alchemist = Alchemist(
            level=level_from_index(18))
        char.culinarian = Culinarian(
            level=level_from_index(19))
        char.miner = Miner(
            level=level_from_index(20))
        char.botanist = Botanist(
            level=level_from_index(21))
        char.fisher = Fisher(
            level=level_from_index(22))

    except (IndexError, ValueError):
        raise ParsingException('Unable to parse id {} from lodestone'.format(lodestone_id))

    return char


def scrape_character_weapons_by_id(lodestone_id):

    logging.debug('Attempting to parse items from id {}'.format(lodestone_id))

    try:
        headers = {'User-Agent': USER_AGENT}
        uri = 'http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(lodestone_id)
        page = requests.get(uri, headers=headers)
        assert page.status_code == 200

    except AssertionError:
        raise ParsingException('Invalid response from Lodestone')

    try:
        tree = html.fromstring(page.text)

        weapon_list = tree.xpath('//div[@class="item_detail_box"]/div/div/div/div/a')
        weapons = []
        for weapon in weapon_list:
            weapons.append(weapon.attrib['href'])

    except (IndexError, ValueError):
        raise ParsingException('Unable to parse item id {} from lodestone'.format(lodestone_id))

    return weapons
