from django.test import TestCase

class CompanydirectoryViewsTestCase(TestCase):
    fixtures = ['initial_data.json']
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

