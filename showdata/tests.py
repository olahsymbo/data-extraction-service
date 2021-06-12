from django.test import TestCase
from django.utils import timezone

from .models import Taskdata


class DataTaskTest(TestCase):
    def setUp(self):
        self.entry = Taskdata.objects.create(
            timestamp=timezone.now().strftime("%Y-%m-%d"),
            temperature="hot",
            duration="ten"
        )

    def test_data_entry(self):
        new_entry = self.entry
        self.assertTrue(isinstance(new_entry, Taskdata))
