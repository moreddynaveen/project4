from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pg(request):
	return HttpResponse('<h2>This page postgraduate information available</h2>')