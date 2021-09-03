"""ultimaAsignatura URL Configuration

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
from django.urls import path
from inicio import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal,name="Index"),
    path('dashboard/',views.dash,name="DashAd"),
    path('crearSolicitud/',views.crear,name="Crear"),
    path('editarSolicitud/<int:id>/',views.editar,name="Editar"),
    path('ver/<int:id>/',views.ver,name="Ver"),
    path('borrar/<int:id>/',views.borrar,name="Borrar")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)