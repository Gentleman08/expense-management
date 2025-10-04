from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit_expense/', views.submit_expense, name='submit_expense'),
    path('expense_history/', views.expense_history, name='expense_history'),
     path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/approve/<int:expense_id>/', views.approve_expense, name='approve_expense'),
    path('manager/reject/<int:expense_id>/', views.reject_expense, name='reject_expense'),

    # Add other URL patterns here as you implement more features
]