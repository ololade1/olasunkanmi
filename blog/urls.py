
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from article import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/',include('accounts.urls')),
    path('',views.welcome,name = 'welcome'),
    path('service/',include('article.urls'))
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()  
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)  