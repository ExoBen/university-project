from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from tulip_wrapper.models import Network
import json


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        # not necessary at the moment
        # self.testNetwork = Network.objects.create(network_name="sas_30_test", network_file="../tulip_wrapper/tests/sas_30.tlp", network_type="TLP");

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
        response = self.client.post(reverse('upload'), {})
        # TO DO

    def tearDown(self):
        return
