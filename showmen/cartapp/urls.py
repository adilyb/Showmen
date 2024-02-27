from django.urls import path
from . views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add/', add, name='add'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),

]
