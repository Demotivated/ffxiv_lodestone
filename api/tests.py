from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Character


class ScrapeFromLodestoneTestCase(TestCase):

    def test_scrape_by_id(self):
        client = Client()
        lodestone_id = '8774791'

        response = client.post(reverse('parse_by_id', kwargs={
            'lodestone_id': lodestone_id
        }))
        self.assertEqual(response.status_code, 200)

        mina = Character.objects.get(lodestone_id=lodestone_id)
        self.assertEqual('Mina Loriel', mina.name)
        self.assertEqual(lodestone_id, mina.lodestone_id, )
        self.assertEqual('Order of the Twin Adder/Second Serpent Lieutenant', mina.grand_company)
        self.assertEqual('Gridania', mina.city_state)
        self.assertEqual('Zanarkand', mina.free_company)
        self.assertEqual('Zalera', mina.server)
        self.assertEqual('Miqo\'te', mina.species)
