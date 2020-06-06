from django.conf.urls import url
from django.contrib import admin
from myapp import views
from django.urls import path
from django.urls import include






urlpatterns=[
    url(r'^admin/',admin.site.urls),

    #url(r'^products/(?P<pk>\d+)/$', views.packageview, name='packageview'),

]



