from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.ProjectsList.as_view(), name='projects'),
    path('contact/', views.contact, name='contacts'),
]
