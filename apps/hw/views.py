from django.shortcuts import render

def index(request):
	print ("Hello world")
	return render(request, 'hw/index.html')