from django.shortcuts import render

import requests
from django.shortcuts import render
from .forms import CityForm

def index(request):
    api_key = '2d2a302e2810c75537582dcd2e6cf7df'  # Replace with your actual API key
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            response = requests.get(url.format(city)).json()

            if response.get('cod') != 200:
                weather_data = {'error': 'City not found!'}
            else:
                weather_data = {
                    'city': city,
                    'temperature': response['main']['temp'],
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                }
    else:
        form = CityForm()
        weather_data = {}

    return render(request, 'index.html', {'form': form, 'weather_data': weather_data})

