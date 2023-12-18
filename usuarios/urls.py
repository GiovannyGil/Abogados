from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.usuarios, name="usuarios"),
    path("NewUsuario/", views.NewUsuario, name="NewUsuario"),
    path("RemoveUsuario/<int:id>/", views.RemoveUsuario, name="RemoveUsuario"),
    path("UpdateUsuario/<int:id>/", views.UpdateUsuario, name="UpdateUsuario"),
    path("DetailUsuario/<int:id>/", views.DetailUsuario, name="DetailUsuario"),
]

urlpatterns += static(settings.MEDIA_URL, document__root=settings.MEDIA_ROOT)
# vincula la ruca de los archivos multimedia
