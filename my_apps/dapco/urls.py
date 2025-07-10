from django.urls import path
from .views import *

app_name = 'dapco'

urlpatterns = [
    path('', index, name='index'),
    path('encuestas/', encuestas_view, name='encuestas'),
]