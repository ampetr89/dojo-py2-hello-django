from django.shortcuts import render
from django.shortcuts import render, HttpResponse


def index(request):
	print (request.method)
	return HttpResponse('Hello World')