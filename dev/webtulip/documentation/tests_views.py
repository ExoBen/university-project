from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from tulip_wrapper.models import Network
import json
from tulip import tlp


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get(reverse('home'), {})
        self.assertEqual(200, response.status_code, 'Wrong status code returned for home')

    def test_more_info(self):
        response = self.client.get(reverse('moreInfo'), {})
        self.assertEqual(200, response.status_code, 'Wrong status code returned for moreInfo')

    def test_delete(self):
        response = self.client.get(reverse('delete'), {})
        self.assertEqual(200, response.status_code, 'Wrong status code returned for delete')

    def test_upload(self):
        with open('tulip_wrapper/tests/g1.tlp') as fp:
            response = self.client.post(reverse('upload'), {'network_name': 'g1test', 'network_file': fp, 'network_type': 'tlp'})
            self.assertEqual(302, response.status_code, 'Wrong status code returned for file upload')
            self.assertEqual("/home", response.url, 'Wrong url returned for file upload')
            network_from_db = Network.objects.get(network_name='g1test')
            test_network = tlp.loadGraph("media/" + network_from_db.network_file.name)
            self.assertEqual(3, len(list(test_network.getNodes())), 'Wrong number of nodes when uploading')
            self.assertEqual(2, len(list(test_network.getEdges())), 'Wrong number of edges when uploading')
            network_from_db.network_file.delete()
            network_from_db.delete()
