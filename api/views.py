from django.http import HttpResponse, HttpResponseServerError
import logging
import re

import requests
from bs4 import BeautifulSoup

from .models import Character


def scrape_by_id(request, lodestone_id):
    page = requests.get('http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(
        lodestone_id
    ))
    try:
        assert page.status_code == 200
    except AssertionError:
        logging.error('Can\'t contact Lodestone')
        return HttpResponseServerError()

    logging.debug('Attempting to parse id {}'.format(lodestone_id))
    html = BeautifulSoup(page.text, 'html.parser')
    char = Character()

    try:
        char.lodestone_id = lodestone_id
        char.name = html.title.string.split('|')[0].strip()

        elements = html.find_all('dd', attrs={
            'class': 'txt_name'
        })
        char.city_state = elements[2].text
        char.grand_company = elements[3].text
        char.free_company = elements[4].text

        char.server = html.find(string=re.compile('^ \([A-Z][a-z]+\)$'))[2:-1]
        char.species = html.find('div', attrs={'class': 'chara_profile_title'}).text.split('/')[0].strip()

        char.save()

    except (IndexError, ValueError):
        logging.error('Unable to parse id {} from lodestone'.format(lodestone_id), exc_info=True)
        return HttpResponseServerError()

    return HttpResponse()
