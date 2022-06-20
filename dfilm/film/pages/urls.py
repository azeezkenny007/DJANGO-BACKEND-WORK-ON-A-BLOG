"""film URL Configuration

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
from django.urls import path,include
from .views import *


urlpatterns = [
    path('404/',error,name='404'),
    path('about/',about,name='about'),
path('catalog1/',catalog1,name='catalog1'),
path('catalog2/',catalog2,name='catalog2'),
path('details1/',details1,name='details1'),
path('details2/',details2,name='details2'),
path('faq/',faq,name='faq'),
path('index/',index,name='index'),
path('index2/',index2,name='index2'),
path('pricing/',pricing,name='pricing'),
]
