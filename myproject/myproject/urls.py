"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from boards import views


urlpatterns = [
    url(r'^/ttt$', views.home, name='home'),

    url(r'^$', views.index,name='index'),

    url(r'^homepage/$', views.home2, name='home2'),
     url(r'^hello/$', views.hello, name='hello'),
    url(r'^admin/', admin.site.urls),
    #url(r'^login/', views.login,name='login'),
    #url(r'^loginform/', views.loginform,name='loginform'),
    path('page1',views.page1),
    path('createForm',views.createForm),
    path('addForm',views.addBlog),
    #url(r'^login/', views.login,name='login'),
    path('login',views.login),
    path('loginform',views.loginform)
    
]
