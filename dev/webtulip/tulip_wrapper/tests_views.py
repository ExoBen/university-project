from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from tulip import tlp

from .models import Network
from .views import loadGraph
from .network_optimiser import NetworkOptimiser
from .tlp_json_converter import TlpJsonConverter

import json

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.testNetwork = Network.objects.create(network_name="sas_30_test", network_file="../tulip_wrapper/tests/sas_30.tlp", network_type="TLP");

    def test_base(self):
        response = self.client.get(reverse('loadGraph'), {'network_name': 'sas_30_test'})
        dict_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(True, dict_response["success"], 'View returned not successful for base')
        self.assertEqual(True, "nodes" in dict_response["data"], 'Nodes not in data for base')
        self.assertEqual(True, "edges" in dict_response["data"], 'Edges not in data for base')
        self.assertEqual(0, len(dict_response["data"]["nodesBeenPruned"]), 'nodesBeenPruned should be empty for base')
        self.assertEqual(0, len(dict_response["data"]["numDeletedClique"]), 'numDeletedClique should be empty for base')
        self.assertEqual(0, len(dict_response["data"]["numDeletedEdge"]), 'numDeletedEdge should be empty for base')

    def test_prune(self):
        response = self.client.get(reverse('loadGraph'), {'network_name': 'sas_30_test', 'toPrune': 'true'})
        dict_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(True, dict_response["success"], 'View returned not successful for pruning')
        self.assertEqual(True, "nodes" in dict_response["data"], 'Nodes not in data for pruning')
        self.assertEqual(True, "edges" in dict_response["data"], 'Edges not in data for pruning')
        self.assertEqual(9, len(dict_response["data"]["nodesBeenPruned"]), 'nodesBeenPruned should have 9 elements for pruning')
        self.assertEqual(0, len(dict_response["data"]["numDeletedClique"]), 'numDeletedClique should be empty for pruning')
        self.assertEqual(0, len(dict_response["data"]["numDeletedEdge"]), 'numDeletedEdge should be empty for pruning')

    def test_edge(self):
        response = self.client.get(reverse('loadGraph'), {'network_name': 'sas_30_test', 'toEdgeBundle': 'true'})
        dict_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(True, dict_response["success"], 'View returned not successful for edge bundling')
        self.assertEqual(True, "nodes" in dict_response["data"], 'Nodes not in data for edge bundling')
        self.assertEqual(True, "edges" in dict_response["data"], 'Edges not in data for edge bundling')
        self.assertEqual(0, len(dict_response["data"]["nodesBeenPruned"]), 'nodesBeenPruned should be empty for edge bundling')
        self.assertEqual(0, len(dict_response["data"]["numDeletedClique"]), 'numDeletedClique should be empty for edge bundling')
        self.assertEqual(3, len(dict_response["data"]["numDeletedEdge"]), 'numDeletedEdge should have 3 elements for edge bundling')

    def test_prune_and_edge(self):
        response = self.client.get(reverse('loadGraph'), {'network_name': 'sas_30_test', 'toEdgeBundle': 'true', 'toPrune': 'true'})
        dict_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(True, dict_response["success"], 'View returned not successful for pruning and edge bundling')
        self.assertEqual(True, "nodes" in dict_response["data"], 'Nodes not in data for pruning and edge bundling')
        self.assertEqual(True, "edges" in dict_response["data"], 'Edges not in data for pruning and edge bundling')
        self.assertEqual(7, len(dict_response["data"]["nodesBeenPruned"]), 'nodesBeenPruned should have 9 elements for pruning and edge bundling')
        self.assertEqual(0, len(dict_response["data"]["numDeletedClique"]), 'numDeletedClique should be empty for pruning and edge bundling')
        self.assertEqual(1, len(dict_response["data"]["numDeletedEdge"]), 'numDeletedEdge should have 1 elements for pruning and edge bundling')

    def test_delete(self):
        response = self.client.post(reverse('deleteGraph'), {'network_name': 'sas_30_test'})
        # still not working - CSRF issue?
        print(response)
        self.assertEqual(200, response.status_code, 'Bad HTTP Response')
        dict_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(True, dict_response["success"], 'deleteFailed')
