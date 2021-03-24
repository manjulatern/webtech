from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Student

# Create your views here.
def index(request):
	template = loader.get_template('student.html')
	return HttpResponse(template.render({}, request))

def search(request):
	keyword = request.GET.get('keyword')

	students = Student.objects.filter(full_name__icontains=keyword)

	context = {"students": students}
	template = loader.get_template('search_result.html')
	return HttpResponse(template.render(context, request))

