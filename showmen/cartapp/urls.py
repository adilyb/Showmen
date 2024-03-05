from django.urls import path
from . views import *

urlpatterns = [
    path('', cart_summary, name='cart'),
    path('add/', add, name='add_cart'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),

]
