from django.test import TestCase
from .tlp_json_converter import TlpJsonConverter
from tulip import tlp

class TlpToJsonTest(TestCase):
    def setUp(self):
        self.g1 = tlp.loadGraph("tulip_wrapper/tests/g1.tlp")
        self.g1_pruned = tlp.loadGraph("tulip_wrapper/tests/g1_pruned.tlp")
        self.sas_30 = tlp.loadGraph("tulip_wrapper/tests/sas_30.tlp")

    def test_g1_basic(self):
        jsonResponse = TlpJsonConverter.tlp_to_json("g1", self.g1, [], [], [])
        self.assertEqual(3, len(jsonResponse["nodes"]), 'The number of nodes is not correct')
        self.assertEqual(2, len(jsonResponse["edges"]), 'The number of edges is not correct')

    def test_sas_30_basic(self):
        jsonResponse = TlpJsonConverter.tlp_to_json("sas_30", self.sas_30, [], [], [])
        self.assertEqual(31, len(jsonResponse["nodes"]), 'The number of nodes is not correct')
        self.assertEqual(26, len(jsonResponse["edges"]), 'The number of edges is not correct')

    def test_g1_prune(self):
        jsonResponse = TlpJsonConverter.tlp_to_json("g1_pruned", self.g1_pruned, [{'number': 2, 'node': self.g1.getOneNode()}], [], [])
        self.assertEqual(1, len(jsonResponse["nodes"]), 'The number of nodes is not correct')
        self.assertEqual(0, len(jsonResponse["edges"]), 'The number of edges is not correct')
        self.assertEqual(2, jsonResponse["nodesBeenPruned"][0]["number"], 'The number of nodes pruned is not correct')
