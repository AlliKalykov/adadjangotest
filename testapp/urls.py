from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('test/', views.model_name_view, name="test")
]
