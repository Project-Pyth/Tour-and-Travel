"""django1_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include

from django.contrib import admin
from django.urls import path
from myapp import views, urls
from django.conf.urls.static import static
from django.conf import settings

from myapp.views import ActivateAccount
admin.site.site_header = "Tour and Travel Admin"
admin.site.site_title = "Tour and Travel Admin Panel"
admin.site.index_title = "Welcome to Tour and Travel Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    url('home/', views.home, name='home'),
    url('index/', views.index, name='index'),
    url('register/', views.register, name='register'),
    url('login/', views.login, name='login'),
    url('thanks/',views.thanks,name='thanks'),
    url('logout/',views.logout ,name='logout'),
    url('profile/', views.view_profile, name='profile'),
    url('showp/', views.seeprofile, name='showp'),
    url('dev_info/', views.dev_info, name='dev_info'),
    url('contact/', views.contact, name='contact'),
    url('booking/', views.booking, name='booking'),
    url('about/', views.about, name='about'),
    url('gallery/',views.view_gallery,name='gallery'),
    url('readmore/',views.readmore,name='readmore'),
    url('blog/',views.blog, name='blog'),
    url('blogpost/', views.blogpost, name='blogpost'),
    url('package/', views.package, name='package'),
    url('allpackages/', views.allpackages, name='allpackages'),
    url('search/', views.search, name='search'),
    url('delhi/', views.delhi, name='delhi'),
    url('chandigarh/', views.chandigarh, name='chandigarh'),
    url('rajasthan/', views.rajasthan, name='rajasthan'),
    url('himachal/', views.himachal, name='himachal'),
    url('cab/', views.cab, name='cab'),
    url('video/', views.video, name='video'),
    url('checkout/', views.checkout, name='checkout'),
    url('handleRequest/', views.handlerequest, name='handle'),
    url('paytm/', views.paymentMode, name='handle'),


    url('package_detail/', views.package_detail, name='package_detail'),


    url('demo/', views.demo, name='demo'),

    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process_payment/', views.process_payment, name='process_payment'),


    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
