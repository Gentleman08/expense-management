from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.db.utils import IntegrityError
from .forms import CustomUserCreationForm, ExpenseClaimForm
from .models import Company, ExpenseClaim
from django.conf import settings

User = settings.AUTH_USER_MODEL

@login_required
def dashboard(request):
    role = request.user.role

    if role == 'EMPLOYEE':
        return redirect('submit_expense')
    elif role == 'MANAGER':
        return redirect('manager_dashboard')
    elif role == 'ADMIN':
        return redirect('admin_dashboard')  # Optional
    else:
        return HttpResponse("Unknown role.")
# Create your views here.
@login_required
def submit_expense(request):
    if request.user.role != 'EMPLOYEE':
        return HttpResponseForbidden("Only employees can submit expenses.")

    if request.method == 'POST':
        form = ExpenseClaimForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.submitter = request.user
            expense.save()
            return redirect('expense_history')
    else:
        form = ExpenseClaimForm()
    return render(request, 'submit_expense.html', {'form': form})

@login_required
def expense_history(request):
    if request.user.role != 'EMPLOYEE':
        return HttpResponseForbidden("Only employees can view their expense history.")

    expenses = ExpenseClaim.objects.filter(submitter=request.user).order_by('-date')
    return render(request, 'expense_history.html', {'expenses': expenses})

@login_required
def manager_dashboard(request):
    if request.user.role not in ['MANAGER', 'ADMIN']:
        return HttpResponseForbidden("Access denied.")

    pending_expenses = ExpenseClaim.objects.filter(
        status='pending',
        submitter__manager=request.user
    ).order_by('date')

    return render(request, 'manager_dashboard.html', {'pending_expenses': pending_expenses})

@login_required
def approve_expense(request, expense_id):
    if request.user.role not in ['MANAGER', 'ADMIN']:
        return HttpResponseForbidden("Access denied.")

    expense = get_object_or_404(ExpenseClaim, pk=expense_id)

    if expense.status == 'pending' and expense.submitter.manager == request.user:
        expense.status = 'approved'
        expense.save()

    return redirect('manager_dashboard')


@login_required
def reject_expense(request, expense_id):
    if request.user.role not in ['MANAGER', 'ADMIN']:
        return HttpResponseForbidden("Access denied.")

    expense = get_object_or_404(ExpenseClaim, pk=expense_id)

    if expense.status == 'pending' and expense.submitter.manager == request.user:
        expense.status = 'rejected'
        expense.save()

    return redirect('manager_dashboard')