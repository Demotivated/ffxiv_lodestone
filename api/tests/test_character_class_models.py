from django.test import TestCase

from ..models import Character, Archer


class CharacterClassTestCase(TestCase):

    def setUp(self):
        self.char = Character()
        self.char.name = 'test character 1'
        self.char.save()

    def test_create_class_associated_with_char(self):
        self.char.archer = Archer(
            level=21
        )

        archer = self.char.archer
        self.assertEqual(archer.level, 21)

        self.char.archer = Archer(
            level=35
        )

        archer = self.char.archer
        self.assertEqual(archer.level, 35)
