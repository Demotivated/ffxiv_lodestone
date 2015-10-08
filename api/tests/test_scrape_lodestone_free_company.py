import logging
import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from api.models import FreeCompany


class ScrapeFromLodestoneTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.lodestone_id = '9229142273877347770'
        self.response = self.client.post(reverse('scrape_free_company_view', kwargs={
            'lodestone_id': self.lodestone_id
        }))
        self.assertEqual(self.response.status_code, 200)

    def test_inside_database(self):
        zanarkand = FreeCompany.objects.get(lodestone_id=self.lodestone_id)
        self.assertEqual('Zanarkand', zanarkand.name)
        self.assertEqual('Zalera', zanarkand.server)
        self.assertEqual('CHAOS', zanarkand.tag)
        self.assertEqual(datetime.date(2013, 10, 19), zanarkand.formed)
        self.assertEqual(8, zanarkand.rank)
        # self.assertEqual(33, zanarkand.weekly_rank)
        # self.assertEqual(45, zanarkand.monthly_rank)
        # self.assertEqual('Burning shit since 2013.', zanarkand.slogan)
        mina = zanarkand.members.get(lodestone_id='8774791')

    # def test_json_response(self):
    #     self.maxDiff = None
    #     self.assertJSONEqual(
    #         self.response.content.decode('utf-8'),
    #         {
    #             "stats": {
    #                 "determination": 26,
    #                 "critical_hit_rate": 0,
    #                 "accuracy": 0,
    #                 "piety": 0,
    #                 "shield_stats": {
    #                     "block_rate": 0,
    #                     "block_strength": 0
    #                 },
    #                 "weapon_stats": {
    #                     "damage": 69,
    #                     "delay": 3.44,
    #                     "auto_attack": 52.74
    #                 },
    #                 "spell_speed": 26,
    #                 "mind": 31,
    #                 "vitality": 32,
    #                 "armor_stats": {
    #                     "defense": 0,
    #                     "magic_defense": 0
    #                 }
    #             },
    #             "lodestone_id": "d19447e548d",
    #             "name": "Thyrus Zenith",
    #             "ilevel": 90,
    #             "type": "Two-handed Conjurer's Arm"
    #         }
    #     )

    def test_invalid_lodestone_id(self):
        logging.disable(logging.CRITICAL)
        response = self.client.post(reverse('scrape_item_view', kwargs={
            'lodestone_id': '91238021830127308189230980912730213821102931255533445521234457172422'
        }))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid response from Lodestone')
        logging.disable(logging.NOTSET)
