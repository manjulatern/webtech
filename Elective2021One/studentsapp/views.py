from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

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

def listStudents(request):
	template = loader.get_template('student_list_datatable.html')
	students = Student.objects.all()
	return HttpResponse(template.render({'students':students}, request))

def listStudentsPaginate(request):
	template = loader.get_template('student_list_paginate.html')
	student_list = Student.objects.all()

	page = request.GET.get('page', 1)
	paginator = Paginator(student_list,3)

	try:
		students =  paginator.page(page)
	except PageNotAnInteger:
		students =  paginator.page(1)
	except EmptyPage:
		students =  paginator.page(paginator.num_pages)

	return HttpResponse(template.render({'students':students}, request))

