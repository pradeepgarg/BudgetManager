from django.contrib import admin
from django.urls import path

from .views import ListTransaction, TransactionViewsets

urlpatterns = [
    path('transactions', TransactionViewsets.as_view({'get': 'list', 'post': 'create'})),
    path('list', ListTransaction.as_view())
]


