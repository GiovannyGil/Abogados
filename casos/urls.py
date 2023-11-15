from os import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern
from django.urls import path
from . import views 

#if settings.DEBUG:
#   URLPattern += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('', views.casos, name="casos"),
    path('AddCaso/', views.AddCaso, name='AddCaso'),
    path('CasoDetail/<int:pk>/', views.CasoDetail, name='CasoDetail'),
    path('CasoRemove/<int:pk>/', views.CasoRemove, name='CasoRemove'),
    path('CasoUpdate/<int:pk>/', views.CasoUpdate, name='CasoUpdate'),
]

urlpatterns += static(settings.MEDIA_URL, document__root=settings.MEDIA_ROOT)
# vincula la ruca de los archivos multimedia