from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from api.models import Character


class ScrapeFromLodestoneTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.lodestone_id = '8774791'
        self.response = self.client.post(reverse('scrape_char_view', kwargs={
            'lodestone_id': self.lodestone_id
        }))
        self.assertEqual(self.response.status_code, 200)

    def test_inside_database(self):
        mina = Character.objects.get(lodestone_id=self.lodestone_id)
        self.assertEqual('Mina Loriel', mina.name)
        self.assertEqual(self.lodestone_id, mina.lodestone_id)
        self.assertEqual('Order of the Twin Adder/Second Serpent Lieutenant', mina.grand_company)
        self.assertEqual('Gridania', mina.city_state)
        self.assertEqual('Zanarkand', mina.free_company)
        self.assertEqual('Zalera', mina.server)
        self.assertEqual('Miqo\'te', mina.species)

    def test_json_response(self):
        self.assertJSONEqual(
            self.response.content.decode('utf-8'),
            {
                "name": "Mina Loriel",
                "lodestone_id": "8774791",
                "grand_company": "Order of the Twin Adder/Second Serpent Lieutenant",
                "city_state": "Gridania",
                "free_company": "Zanarkand",
                "server": "Zalera",
                "species": "Miqo'te",
                "classes": {
                    "carpenter": 50,
                    "goldsmith": 50,
                    "marauder": 0,
                    "gladiator": 0,
                    "conjurer": 50,
                    "botanist": 20,
                    "blacksmith": 18,
                    "weaver": 50,
                    "leatherworker": 16,
                    "astrologian": 0,
                    "culinarian": 37,
                    "arcanist": 50,
                    "rogue": 0,
                    "dark_night": 0,
                    "armorer": 15,
                    "archer": 9,
                    "miner": 0,
                    "thaumaturge": 26,
                    "machinist": 0,
                    "pugilist": 0,
                    "alchemist": 16,
                    "fisher": 0,
                    "lancer": 6
                },
            }
        )

    def test_invalid_lodestone_id(self):
        response = self.client.post(reverse('scrape_char_view', kwargs={
            'lodestone_id': '91238298371293791287391827317314422'
        }))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid response from Lodestone')
