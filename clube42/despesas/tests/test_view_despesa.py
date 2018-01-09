from django.test import TestCase


class DespesaTest(TestCase):

    def test_get(self):
        resp = self.client.get('/despesas/')
        self.assertEqual(200, resp.status_code)