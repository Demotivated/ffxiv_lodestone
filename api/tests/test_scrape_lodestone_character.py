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
        self.assertEqual('Order of the Twin Adder/Second Serpent Lieutenant', mina.grand_company)
        self.assertEqual('Gridania', mina.city_state)
        self.assertEqual('Zanarkand', mina.free_company)
        self.assertEqual('Zalera', mina.server)
        self.assertEqual('Miqo\'te', mina.species)

    def test_json_response(self):
        self.maxDiff = None
        self.assertJSONEqual(
            self.response.content.decode('utf-8'),
            {
                "free_company": "Zanarkand",
                "name": "Mina Loriel",
                "species": "Miqo'te",
                "grand_company": "Order of the Twin Adder/Second Serpent Lieutenant",
                "server": "Zalera",
                "lodestone_id": "8774791",
                "city_state": "Gridania",
                "classes": {
                    "armorer": {
                        "level": 15
                    },
                    "alchemist": {
                        "level": 16
                    },
                    "leatherworker": {
                        "level": 16
                    },
                    "pugilist": {
                        "level": 0
                    },
                    "carpenter": {
                        "level": 50
                    },
                    "culinarian": {
                        "level": 37
                    },
                    "arcanist": {
                        "level": 50
                    },
                    "fisher": {
                        "level": 0
                    },
                    "machinist": {
                        "level": 0
                    },
                    "conjurer": {
                        "level": 50
                    },
                    "blacksmith": {
                        "level": 18
                    },
                    "astrologian": {
                        "level": 0
                    },
                    "thaumaturge": {
                        "level": 26
                    },
                    "gladiator": {
                        "level": 0
                    },
                    "miner": {
                        "level": 0
                    },
                    "lancer": {
                        "level": 6
                    },
                    "rogue": {
                        "level": 0
                    },
                    "marauder": {
                        "level": 0
                    },
                    "botanist": {
                        "level": 20
                    },
                    "weaver": {
                        "level": 50
                    },
                    "archer": {
                        "level": 9
                    },
                    "darknight": {
                        "level": 0
                    },
                    "goldsmith": {
                        "level": 50
                    }
                }
            }
        )

    def test_invalid_lodestone_id(self):
        response = self.client.post(reverse('scrape_character_view', kwargs={
            'lodestone_id': '91238298371293791287391827317314422'
        }))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid response from Lodestone')
