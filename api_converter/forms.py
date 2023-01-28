import requests
from django import forms


class ConverterForm(forms.Form):
    # url = 'https://api.exchangerate.host/latest'
    # response = requests.get(url)
    # data = response.json()
    # data = [*data['rates']]
    # currencies = [(i, i) for i in data]

    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    data = data['symbols']
    currencies = [(i, f'{j["description"]} ({i})') for i, j in data.items()]

    input_currency_combobox = forms.ChoiceField(label='From', choices=currencies,
                                                widget=forms.Select(attrs={'class': "form-control"}))
    input_currency_entry = forms.IntegerField(label='Amount',
                                              widget=forms.NumberInput(
                                                  attrs={'placeholder': 'input amount', 'class': 'form-control'}))
    output_currency_combobox = forms.ChoiceField(label='To', choices=currencies,
                                                 widget=forms.Select(attrs={'class': "form-control"}))

    output_currency_entry = forms.IntegerField(label='Result', disabled=True, required=False,
                                               widget=forms.NumberInput(
                                                   attrs={'placeholder': 'result will be here',
                                                          'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ConverterForm, self).__init__(*args, **kwargs)
        self.initial['input_currency_combobox'] = 'USD'
        self.initial['output_currency_combobox'] = 'USD'
