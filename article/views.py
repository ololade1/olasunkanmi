from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Article,Service
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms



def services (request):
	articles = Article.objects.all().order_by('date')
	return render(request,'articles/service_list.html',{'clients':clients})
def service_detail (request,slug):
	#return HttpResponse(slug)
	article = Article.objects.get(slug = slug)
	return render(request,'articles/service_detail.html',{'client':client})

@login_required(login_url = "/accounts/login")   
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			# save article to db
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()
			return redirect('articles:services')

	else:
		form = forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form':form })
	   