import logging

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from api.models import Character


class ScrapeFromLodestoneTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.lodestone_id = '8774791'
        self.response = self.client.post(reverse('scrape_character_view', kwargs={
            'lodestone_id': self.lodestone_id
        }))
        self.assertEqual(self.response.status_code, 200)

    def test_inside_database(self):
        mina = Character.objects.get(lodestone_id=self.lodestone_id)
        self.assertEqual('Mina Loriel', mina.name)
        self.assertEqual(self.lodestone_id, mina.lodestone_id)
        self.assertEqual('Order of the Twin Adder', mina.grand_company_name)
        self.assertEqual('Second Serpent Lieutenant', mina.grand_company_rank)
        self.assertEqual('Gridania', mina.city_state)
        self.assertEqual('Zanarkand', mina.free_company_name)
        self.assertEqual('9229142273877347770', mina.free_company_id)
        self.assertEqual('Zalera', mina.server)
        self.assertEqual('Miqo\'te', mina.species)

    def test_invalid_lodestone_id(self):
        logging.disable(logging.CRITICAL)
        response = self.client.post(reverse('scrape_character_view', kwargs={
            'lodestone_id': '91238298371293791287391827317314422'
        }))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid response from Lodestone')
        logging.disable(logging.NOTSET)
