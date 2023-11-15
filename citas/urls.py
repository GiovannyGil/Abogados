from django.urls import path

from . import views

urlpatterns = [
    path("", views.citas, name="citas"),
    path('AddCita/', views.AddCita, name='AddCita'),
    path('CitaDetail/<int:pk>/', views.CitaDetail, name='CitaDetail'),
    path('CitaRemove/<int:pk>/', views.CitaRemove, name='CitaRemove'),
    path('CitaUpdate/<int:pk>/', views.CitaUpdate, name='CitaUpdate'),
]
