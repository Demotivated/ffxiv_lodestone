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
                "grand_company": {
                    "name": "Order of the Twin Adder",
                    "rank": "Second Serpent Lieutenant"
                },
                "server": "Zalera",
                "lodestone_id": "8774791",
                "city_state": "Gridania",
                "jobs": [
                    {
                        'job': 'White Mage',
                        'level': 50,
                        "items": [
                            {
                                "lodestone_id": "d19447e548d",
                                "name": "Thyrus Zenith"
                            },
                            {
                                "lodestone_id": "fa0a11eb218",
                                "name": "Platinum Circlet of Healing"
                            },
                            {
                                "lodestone_id": "cada9ec7074",
                                "name": "Arachne Robe"
                            },
                            {
                                "lodestone_id": "ec2ddbdcd47",
                                "name": "Weathered Daystar Gloves"
                            },
                            {
                                "lodestone_id": "3f4a40dca32",
                                "name": "Weathered Daystar Belt"
                            },
                            {
                                "lodestone_id": "8a049823b22",
                                "name": "Weathered Daystar Breeches"
                            },
                            {
                                "lodestone_id": "6bfac2114ef",
                                "name": "Weathered Daystar Sollerets"
                            },
                            {
                                "lodestone_id": "a2e77d6e599",
                                "name": "Emerald Choker"
                            },
                            {
                                "lodestone_id": "3ef1897edbb",
                                "name": "Emerald Earrings"
                            },
                            {
                                "lodestone_id": "ec78b3a439e",
                                "name": "Weathered Daystar Armillae"
                            },
                            {
                                "lodestone_id": "946b83ef9c4",
                                "name": "Emerald Ring"
                            },
                            {
                                "lodestone_id": "9cca5eb0fd2",
                                "name": "Soul of the White Mage"
                            }
                        ],
                    }
                ],
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
        logging.disable(logging.CRITICAL)
        response = self.client.post(reverse('scrape_character_view', kwargs={
            'lodestone_id': '91238298371293791287391827317314422'
        }))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid response from Lodestone')
        logging.disable(logging.NOTSET)
