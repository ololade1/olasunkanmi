from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader


	
def welcome(request):
	return render(request,'blog/welcome.html')

	 