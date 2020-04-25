from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)


from .models import Transaction

from .serializers import (
    TransactionSerializer,
    UserSerializer,
    MonthlyBudgetSerializer,
)


class TransactionViewset(
    viewsets.GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class UserViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = UserSerializer


class MonthlyBudgetViewset(
    viewsets.GenericViewSet,
    ListModelMixin, CreateModelMixin, RetrieveModelMixin
):
    serializer_class = MonthlyBudgetSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
