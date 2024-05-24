from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('upload/', views.upload_file, name='upload_file'),
]

