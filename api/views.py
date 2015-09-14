from django.http import HttpResponse, HttpResponseServerError
import logging
import re

import requests
from bs4 import BeautifulSoup

from .models import Character
from .exceptions import ParsingException


def scrape_by_id(request, lodestone_id):
    try:
        logging.debug('Attempting to parse id {}'.format(lodestone_id))

        try:
            page = requests.get('http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(
                lodestone_id
            ))
            assert page.status_code == 200
        except AssertionError:
            raise ParsingException('Can\'t contact Lodestone')

        try:
            char = Character()
            html = BeautifulSoup(page.text, 'html.parser')
            elements = html.find_all('dd')

            char.lodestone_id = lodestone_id
            char.name = html.title.string.split('|')[0].strip()
            char.city_state = elements[5].text
            char.grand_company = elements[7].text
            char.free_company = elements[9].text
            char.server = html.find(string=re.compile('^ \([A-Z][a-z]+\)$'))[2:-1]
            char.species = html.find('div', attrs={'class': 'chara_profile_title'}).text.split('/')[0].strip()

            char.save()
        except (IndexError, ValueError):
            raise ParsingException('Unable to parse id {} from lodestone'.format(lodestone_id))

    except ParsingException as e:
        return HttpResponseServerError(e.message)

    return HttpResponse()
