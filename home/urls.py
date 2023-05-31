from .views import *
from django.urls import path

urlpatterns = [
    path('', Home, name='home'),
    path('add/', ADD, name='add'),
    path('edit/', EDIT, name='edit'),
    path('update/<str:id>', UPDATE, name='update'),
    path('delete/<str:id>', DELETE, name='delete'),
]
