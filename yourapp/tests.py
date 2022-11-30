from django.test import TestCase
from django.shortcuts import reverse


class YourAppTestCase(TestCase):

    def test_one_plus_one(self):
        self.assertTrue(1 + 1, 2)

    def test_some_endpoint(self):
        url = reverse('some-endpoint')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['message'], 'Hello, World!')
