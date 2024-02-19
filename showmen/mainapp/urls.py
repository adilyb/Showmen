from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='index'),
    path('', views.category_list, name='category_list'),
    path('<slug:slug_url>/', views.store, name='home_page'),
    path('<slug:slug_url>/<slug:product_slug>', views.product_view, name='product_detail_view'),
    path('search', views.search, name='search'),
    
]