from rest_framework import routers

from .views import (
    TransactionViewset,
    MonthlyBudgetViewset
   )

router = routers.SimpleRouter()

router.register(r'transactions', TransactionViewset, basename='transactions')
router.register(
    r'monthly-budgets',
    MonthlyBudgetViewset,
    basename='monthly-budgets'
)


urlpatterns = router.urls
