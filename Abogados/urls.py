"""
URL configuration for Abogados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import statistics
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("casos/", include('casos.urls')),
    path("", include('base.urls')),
    path("clientes/", include('clientes.urls')),
    path("citas/", include('citas.urls')),
    path("dash", include('dash.urls')),
    path("login/", include('login.urls')),
    path("perfil/", include('perfiles.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # vinvula para la ruta de los archivos multimedia en el admin 



#if settings.DEBUG:
    #from django.conf.urls.static import static 
    #urlpatterns += statistics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    URLPattern += statistics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
