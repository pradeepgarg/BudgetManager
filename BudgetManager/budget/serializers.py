from rest_framework import serializers
from .models import MonthlyBudget, Transaction, CustomCategory
from budget_user.models import BudgetUser

class TransactionSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaction
        fields = ('amount', 'type', 'category','description', 'is_recurring','user')
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetUser
        fields = ('username', 'email')

