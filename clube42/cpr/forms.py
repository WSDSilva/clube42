from django import forms


class DespesaForm(forms.Form):
    categorias = forms.ChoiceField(label='Categorias',
                                   choices=(
                                       ('1', 'Custos'),
                                       ('2', 'Despesas Administrativas'),
                                       ('3', 'Despesas Comerciais'),
                                       ('4', 'Despesas Financeiras'),
                                       ('5', 'Despesas Operacionais'),
                                       ('6', 'Folha'),
                                       ('7', 'Impostos Sobre Faturamento')))

    descricao = forms.CharField(label='Descrição')
