from django.urls import path
from .views import *

urlpatterns = [
    path('', myview5, name='myviewpage'),
]
