import requests

from django.test import TestCase, Client

from ..constants import USER_AGENT


class ScrapeFromLodestoneTestCase(TestCase):

    def test_scrape_by_id(self):
        lodestone_id = '8774791'

        headers = {'User-Agent': USER_AGENT}
        uri = 'http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(lodestone_id)
        page = requests.get(uri, headers=headers)
        text = page.text

        self.assertIn('Mina Loriel', text)
        self.assertIn('Order of the Twin Adder/Second Serpent Lieutenant', text)
        self.assertIn('Gridania', text)
        self.assertIn('Zanarkand', text)
        self.assertIn('Zalera', text)
        self.assertIn('Miqo&#39;te', text)
