from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.store, name='index'),
    #  path('<slug:categ_slug_var>/', views.store, name='prod_cat'),
]