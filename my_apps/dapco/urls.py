from django.urls import path
from .views import *

app_name = 'dapco'

urlpatterns = [
    path('', index, name='index'),
    path('encuestas/', encuestas_view, name='encuestas'),
    path('encuestas/<int:encuesta_id>/', encuesta_detail_view, name='encuesta_detail'),
    path('encuestas/cuotas/<int:encuesta_id>/', cuotas_encuesta_view, name='cuotas_encuesta'),
    path('not-found/', not_found_view, name='not_found'),
]