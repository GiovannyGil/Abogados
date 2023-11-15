
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.perfil, name="perfil"),
    # path('profile/<int:user_id>/', views.update_profile, name='update_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # vinvula para la ruta de los archivos multimedia en el admin