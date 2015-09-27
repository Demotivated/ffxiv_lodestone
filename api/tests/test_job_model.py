from django.test import TestCase

from ..models import Character, Job
from ..constants import JOBS


class CharacterClassTestCase(TestCase):

    def setUp(self):
        self.char = Character()
        self.char.name = 'test character 2'
        self.char.lvl_lancer = 41
        self.char.lvl_armorer = 10
        self.char.save()

    def test_classless_job(self):
        dragoon = self.char.job_set.create(
            job=JOBS.DRAGOON.name
        )
        dragoon.save()

        dragoon = self.char.job_set.get(job=JOBS.DRAGOON.name)
        self.assertEqual(dragoon.level, 41)

    def test_class_with_job(self):
        armorer = self.char.job_set.create(
            job=JOBS.ARMORER.name
        )
        armorer.save()

        armorer = self.char.job_set.get(job=JOBS.ARMORER.name)
        self.assertEqual(armorer.level, 10)
