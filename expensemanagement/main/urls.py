from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('add_user', views.add_user, name='add_user'),
    path('payment', views.payment, name='payment'),
    path('transactions', views.transactions, name='transactions'),
]