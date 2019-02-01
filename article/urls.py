  
 
from django.urls import path,re_path,include
from . import views
app_name = 'article'
urlpatterns = [
    
    path('services/',views.services,name = "services"),
    re_path(r'^create/$',views.article_create,name = 'create'),  
    re_path(r'^(?P<slug>[\w-]+)/$',views.service_detail,name = 'detail'),
]
 