# expenses/urls.py
# manager/urls.py
from django.urls import path
from .views import (
    dashboard,
    submit_expense,
    expense_history,
    manager_dashboard,
    approve_expense,
    reject_expense,
)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('submit-expense/', submit_expense, name='submit_expense'),
    path('expense-history/', expense_history, name='expense_history'),
    path('manager-dashboard/', manager_dashboard, name='manager_dashboard'),
    path('approve/<int:expense_id>/', approve_expense, name='approve_expense'),
    path('reject/<int:expense_id>/', reject_expense, name='reject_expense'),
]