from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candy', views.show, name='show'),
]
