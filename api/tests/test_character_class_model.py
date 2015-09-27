from django.test import TestCase

from ..models import Character


class CharacterClassTestCase(TestCase):

    def setUp(self):
        self.char = Character()
        self.char.name = 'test character 1'
        self.char.lvl_archer = 21
        self.char.save()

    def test_get_and_update_char(self):
        self.char.lvl_archer = 35
        self.char.save()

        archer = Character.objects.get(id=self.char.id)
        self.assertEqual(archer.lvl_archer, 35)

        archer.lvl_archer = 21
        archer.save()

        archer = Character.objects.get(id=self.char.id)
        self.assertEqual(archer.lvl_archer, 21)
