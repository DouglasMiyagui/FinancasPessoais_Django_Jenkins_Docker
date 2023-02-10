from django.urls import path
from usuarios.views import *

urlpatterns=[
    path('cadastrar_usuario', cadastrar_usuario, name='cadastrar_usuario'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
]
