from django.urls import path
from . views import *

urlpatterns = [
    path('', cart_summary, name='cart'),
    path('add/', add, name='add_cart'),
    path('update/', update_cart, name='update_cart'),
    path('delete/', delete, name='delete'),

]
