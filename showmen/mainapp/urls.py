from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='index'),
    path('', views.cat, name='cat'),
    path('<slug:slug_url>/', views.store, name='categ'),
    
    
]