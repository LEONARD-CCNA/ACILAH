# mkif_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
    path('research/', views.research_list, name='research_list'),
    path('projects/', views.project_list, name='project_list'),
    path('communications/', views.communication_list, name='communication_list'),
]
