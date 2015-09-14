import requests

from django.test import TestCase, Client


class ScrapeFromLodestoneTestCase(TestCase):

    def test_scrape_by_id(self):
        lodestone_id = '8774791'

        page = requests.get('http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(
            lodestone_id
        ))
        text = page.text

        self.assertIn('Mina Loriel', text)
        self.assertIn('Order of the Twin Adder/Second Serpent Lieutenant', text)
        self.assertIn('Gridania', text)
        self.assertIn('Zanarkand', text)
        self.assertIn('Zalera', text)
        self.assertIn('Miqo\'te', text)
