from django.http import HttpResponse
import logging

import requests
from lxml import html

from .models import Character


def parse_by_id(request, lodestone_id):
    page = requests.get('http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(
        lodestone_id
    ))
    logging.debug('Attempting to parse id {}'.format(lodestone_id))
    # tree = html.fromstring(page.text)
    tree = html.fromstring(page.text)

    char = Character()
    char.lodestone_id = lodestone_id
    char.name = tree.xpath('//title/text()')[0].split('|')[0].strip()

    info = tree.xpath('//dl[@class="chara_profile_box_info clearfix"]//dd[@class="txt_name"]/text()')
    _, _, char.city_state, char.grand_company = info

    char.free_company = tree.xpath('//dd[@class="txt_name"]/a[contains(@href, "")]/text()')[0]

    char.server = tree.xpath('//h2//span/text()')[0].strip()[1:-1]

    info = tree.xpath('//div[@class="chara_profile_title"]')
    species, _, _ = info[0].text.split('/')
    char.species = species.strip()

    char.save()
    return HttpResponse()
