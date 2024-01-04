from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.store, name='index'),
    path('<slug:slug_url>/', views.store, name='categ'),
]