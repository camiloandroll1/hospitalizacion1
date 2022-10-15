"""hospitalizacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('medico/', views.MedicoCreateView.as_view()),
    path('medico/<int:pk>/', views.MedicoDetailView.as_view()),
    path('enfermero/', views.EnfermeroCreateView.as_view()),
    path('enfermero/<int:pk>/', views.EnfermeroDetailView.as_view()),
    path('familiar/', views.FamiliarCreateView.as_view()),
    path('familiar/<int:pk>/', views.FamiliarDetailView.as_view()),
    path('historiaClinica/', views.HistoriaClinicaCreateView.as_view()),
    path('historiaClinica/<int:pk>/', views.HistoriaClinicaDetailView.as_view()),
    path('paciente/', views.PacienteCreateView.as_view()),
    path('paciente/<int:pk>/', views.PacienteDetailView.as_view()),
]