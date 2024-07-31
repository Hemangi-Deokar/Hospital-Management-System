from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hospitals/', views.hospital_list, name='hospitals'),
    path('hospitals/<int:pk>/', views.hospital_detail, name='hospital_detail'),
    path('hospitals/<int:pk>/appointment/', views.make_appointment, name='make_appointment'),
]
