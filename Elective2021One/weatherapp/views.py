from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import requests

WEATHER_API_KEY = '63ad24b403c944e6be125338210104'
# Create your views here.
def index(request):
	template = loader.get_template('weather_home.html')
	return HttpResponse(template.render({}, request))

def search(request):
	template = loader.get_template('weather_data.html')

	city = request.GET.get('city')
	response = requests.get('http://api.weatherapi.com/v1/current.json?key='+WEATHER_API_KEY+'&q='+city)

	weather = response.json()

	return HttpResponse(template.render({"weather":weather}, request))