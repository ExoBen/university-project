from django.test import TestCase
from .network_optimiser import NetworkOptimiser
from tulip import tlp

class OptimiserTest(TestCase):
    def setUp(self):
        self.g1 = tlp.loadGraph("tulip_wrapper/tests/g1.tlp")
        self.g2 = tlp.loadGraph("tulip_wrapper/tests/g2.tlp")
        self.sas_30 = tlp.loadGraph("tulip_wrapper/tests/sas_30.tlp")

    def test_g1_pruning(self):
        self.assertEqual(3, len(list(self.g1.getNodes())), 'Number of nodes before pruning is wrong - g1')
        self.assertEqual(2, len(list(self.g1.getEdges())), 'Number of edges before pruning is wrong - g1')
        g1_pruned = NetworkOptimiser.nodePruning(self.g1)[0]

        self.assertEqual(1, len(list(g1_pruned.getNodes())), 'Number of nodes after pruning is wrong - g1')
        self.assertEqual(0, len(list(g1_pruned.getEdges())), 'Number of edges after pruning is wrong - g1')

    def test_sas_30_pruning(self):
        self.assertEqual(31, len(list(self.sas_30.getNodes())), 'Number of nodes before pruning is wrong - sas_30')
        self.assertEqual(26, len(list(self.sas_30.getEdges())), 'Number of edges before pruning is wrong - sas_30')
        sas_30_pruned = NetworkOptimiser.nodePruning(self.sas_30)[0]

        self.assertEqual(9, len(list(sas_30_pruned.getNodes())), 'Number of nodes after pruning is wrong - sas_30')
        self.assertEqual(4, len(list(sas_30_pruned.getEdges())), 'Number of edges after pruning is wrong - sas_30')


    def test_g1_edge_bundling(self):
        self.assertEqual(3, len(list(self.g1.getNodes())), 'Number of nodes before edge bundling is wrong - g1')
        self.assertEqual(2, len(list(self.g1.getEdges())), 'Number of edges before edge bundling is wrong - g1')
        g1_edge = NetworkOptimiser.edgeBasedNodeBundling(self.g1)[0]

        self.assertEqual(3, len(list(g1_edge.getNodes())), 'Number of nodes after edge bundling is wrong - g1')
        self.assertEqual(2, len(list(g1_edge.getEdges())), 'Number of edges after edge bundling is wrong - g1')

    def test_sas_30_edge_bundling(self):
        self.assertEqual(31, len(list(self.sas_30.getNodes())), 'Number of nodes before edge bundling is wrong - sas_30')
        self.assertEqual(26, len(list(self.sas_30.getEdges())), 'Number of edges before edge bundling is wrong - sas_30')
        sas_30_pruned = NetworkOptimiser.edgeBasedNodeBundling(self.sas_30)[0]

        self.assertEqual(18, len(list(sas_30_pruned.getNodes())), 'Number of nodes after edge bundling is wrong - sas_30')
        self.assertEqual(13, len(list(sas_30_pruned.getEdges())), 'Number of edges after edge bundling is wrong - sas_30')


    def test_g1_clique_bundling(self):
        self.assertEqual(6, len(list(self.g2.getNodes())), 'Number of nodes before clique bundling is wrong - g2')
        self.assertEqual(10, len(list(self.g2.getEdges())), 'Number of edges before clique bundling is wrong - g2')
        g2_clique = NetworkOptimiser.cliqueBasedNodeBundling(self.g2)[0]

        self.assertEqual(4, len(list(g2_clique.getNodes())), 'Number of nodes after clique bundling is wrong - g2')
        self.assertEqual(7, len(list(g2_clique.getEdges())), 'Number of edges after clique bundling is wrong - g2')
