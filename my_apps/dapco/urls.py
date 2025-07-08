from django.urls import path
from .views import *

app_name = 'dapco'

urlpatterns = [
    path('', index, name='index'),
]