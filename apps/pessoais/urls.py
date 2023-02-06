from django.urls import path
from pessoais.views.analises import *

urlpatterns = [
    path('', index, name='index'),
]