from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product, UserProduct
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def index(request):
	template = loader.get_template('shop.html')

	products = Product.objects.all()
	return HttpResponse(template.render({'products':products}, request))