
from django.test import TestCase

from .models import ElectricityUsage


class ElectricityUsageModelTests(TestCase):

    def test_set_watts_cannot_be_less_than_zero(self):
        test_watts = -1
        elec_usage = ElectricityUsage()
        elec_usage.watts = 1
        elec_usage.set_watts(test_watts)
        self.assertIs(elec_usage.watts, 0)