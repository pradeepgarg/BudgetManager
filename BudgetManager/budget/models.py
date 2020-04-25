from django.db import models
from budget_user.models import BudgetUser
from BudgetManager.models import BudgetManagerBaseModel


class MonthlyBudget(BudgetManagerBaseModel):
    user = models.ForeignKey(
        BudgetUser, on_delete=models.CASCADE, related_name='monthly_budgets'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(BudgetManagerBaseModel):
    CATEGORIES = (
        ('S', 'Salary'),
        ('P', 'Personal'),
        ('R', 'Rent'),
        ('F', 'Food'),
        ('B', 'Bills'),
        ('O', 'Others'),
    )
    TYPES = (
        ('C', 'Credit'),
        ('D', 'Debit'),
    )
    user = models.ForeignKey(
        BudgetUser, on_delete=models.CASCADE, related_name='transactions'
    )
    amount = models.FloatField(max_length=20)
    type = models.CharField(choices=TYPES, max_length=1)
    category = models.CharField(choices=CATEGORIES, max_length=1)
    description = models.CharField(max_length=30)
    is_recurring = models.BooleanField()


class CustomCategory(BudgetManagerBaseModel):
    user = models.ForeignKey(
        BudgetUser, on_delete=models.CASCADE, related_name='custom_categories'
    )
    name = models.CharField(max_length=30)
