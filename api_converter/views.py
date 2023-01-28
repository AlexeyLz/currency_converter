import requests
from django.shortcuts import render


# Create your views here.
from api_converter.forms import ConverterForm


def index(request):
    if 'convert_button' in request.POST:
        form = ConverterForm(request.POST)

        if form.is_valid():
            input_currency_combobox = form.cleaned_data.get('input_currency_combobox')

            input_currency_entry = form.cleaned_data['input_currency_entry']
            output_currency_combobox = form.cleaned_data['output_currency_combobox']

            url = f'https://api.exchangerate.host/convert?from={input_currency_combobox}&to={output_currency_combobox}' \
                  f'&amount={input_currency_entry} '
            response = requests.get(url)
            data = response.json()

            form = ConverterForm(request.POST)
            form.fields['output_currency_entry'].initial = round(float(data['result']), 2)

            context = {'form': form}
            return render(request, 'index.html', context)
    form = ConverterForm()
    context = {'form': form}
    return render(request, 'index.html', context)