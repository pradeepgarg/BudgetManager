from django.shortcuts import render
from .models import Transaction
from .serializers import TransactionSerializer, UserSerializer
from rest_framework import generics, viewsets


# Create your views here.
class ListTransaction(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionViewsets(viewsets.ModelViewSet):
    #queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    def get_queryset(self):
        """
        This view should return transactions for the currently authenticated user.
        """
        user = self.request.user
        return Transaction.objects.filter(user_id=user) 
    

class UserViewsets(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = UserSerializer
