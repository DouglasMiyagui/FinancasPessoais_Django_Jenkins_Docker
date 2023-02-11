from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('pessoais.urls')),
    path('usuario/', include('usuarios.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
