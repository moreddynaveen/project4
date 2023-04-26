from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inter(request):
	return HttpResponse('<h1>This page inter colleges information available</h1>')