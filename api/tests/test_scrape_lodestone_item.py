import logging

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from api.models import Item


class ScrapeFromLodestoneTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.lodestone_id = 'd19447e548d'
        self.response = self.client.post(reverse('scrape_item_view', kwargs={
            'lodestone_id': self.lodestone_id
        }))
        self.assertEqual(self.response.status_code, 200)

    def test_inside_database(self):
        thyrus = Item.objects.get(lodestone_id=self.lodestone_id)
        self.assertEqual('Thyrus Zenith', thyrus.name)
        self.assertEqual(self.lodestone_id, thyrus.lodestone_id)
        self.assertEqual(90, thyrus.item_level)
        self.assertEqual('Two-handed Conjurer\'s Arm', thyrus.item_type)

    def test_json_response(self):
        self.maxDiff = None
        self.assertJSONEqual(
            self.response.content.decode('utf-8'),
            {
                "stats": {
                    "damage": 69,
                    "delay": 3.44,
                    "auto_attack": 52.74
                },
                "lodestone_id": "d19447e548d",
                "name": "Thyrus Zenith",
                "ilevel": 90,
                "type": "Two-handed Conjurer's Arm"
            }
        )

    def test_invalid_lodestone_id(self):
        logging.disable(logging.CRITICAL)
        response = self.client.post(reverse('scrape_item_view', kwargs={
            'lodestone_id': '912382983712x937c9128739t1827a317314422'
        }))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid response from Lodestone')
        logging.disable(logging.NOTSET)
