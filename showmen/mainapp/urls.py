from django.urls import path
from . import views

urlpatterns = [
    path('index', views.store, name='index'),
    #  path('store', views.store, name='store'),
]