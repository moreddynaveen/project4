from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def school(request):
	return HttpResponse('<h2>This page school information available</h2>')