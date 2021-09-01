
from django.urls import path,include
from .views import *

urlpatterns = [    
    path('',HomePage, name='home-page'),
    path('register/',Register, name='register-page')
]