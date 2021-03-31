from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("search/", views.search,name="search"),
    path("list/", views.listStudents,name="listStudents"),
    path("paginate/", views.listStudentsPaginate,name="listStudentsPaginate"),
    ]