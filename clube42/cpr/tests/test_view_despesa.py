from django.test import TestCase
from clube42.cpr.forms import DespesaForm


class DespesaTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/despesas/')
        self.form = DespesaForm()

    def test_get(self):
        """/despesas/ deve retornar status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ deve usar despesas/despesas.html"""
        self.assertTemplateUsed(self.resp, 'despesas/despesa.html')

    def test_html(self):
        """deve conter input tags"""
        tags = (('<form', 1),
                ('<select', 1),
                ('<input', 4),
                ('type="button"', 1),
                ('type="submit"', 1),
                ('type="text"', 1))

        for texto, quant in tags:
            with self.subTest():
                self.assertContains(self.resp, texto, quant)

    def test_csrf(self):
        """html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form(self):
        """Deve ter form de despesas no contexto"""
        self.assertIsInstance(self.form, DespesaForm)

    def test_form_has_fields(self):
        """Deve ter 2 campos"""
        expected = ['categorias', 'descricao']
        self.assertSequenceEqual(expected, list(self.form.fields))
