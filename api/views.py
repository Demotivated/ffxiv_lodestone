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

            char.save()
        except (IndexError, ValueError):
            raise ParsingException('Unable to parse id {} from lodestone'.format(lodestone_id))

    except ParsingException as e:
        return HttpResponseServerError(e.message)

    return JsonResponse(char.as_dict())
