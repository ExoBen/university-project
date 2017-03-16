from django.test import TestCase

from .models import network

from .network_optimiser import NetworkOptimiser
from .tlp_json_converter import TlpJsonConverter

from tulip import tlp

class OptimiserTest(TestCase):
    def setUp(self):


    def test_1(self):
        self.response = client.get(reverse('loadGraph'), {'q': 'DJ'})
