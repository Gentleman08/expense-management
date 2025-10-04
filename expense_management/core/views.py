# core/views.py

import requests
from django.shortcuts import render, redirect ,  get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm , ExpenseClaimForm
from .models import Company, User , ExpenseClaim
from django.db.utils import IntegrityError
from django.http import HttpResponseForbidden
from django.http import HttpResponse

def dashboard(request):
    """
    Placeholder for the user dashboard.
    """
    return HttpResponse("This is the dashboard page.")


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Check if a company and admin user already exist
                if not Company.objects.exists():
                    # Fetch country and currency data from the API
                    try:
                        response = requests.get("https://restcountries.com/v3.1/all?fields=name,currencies")
                        data = response.json()
                        country_data = data[0]  # Use the first country for simplicity
                        country_name = country_data['name']['common']
                        currency_code = list(country_data['currencies'].keys())[0]

                        # Create the Company and Admin User
                        company = Company.objects.create(name=f"{country_name} Corp", currency=currency_code)
                        user = form.save(commit=False)
                        user.role = 'admin'
                        user.company = company
                        user.save()

                        # Log the admin in
                        login(request, user)
                        return redirect('dashboard')

                    except requests.exceptions.RequestException:
                        # Handle API error by creating a default company
                        company = Company.objects.create(name="Default Corp", currency="USD")
                        user = form.save()
                        user.role = 'admin'
                        user.company = company
                        user.save()
                        login(request, user)
                        return redirect('dashboard')

                else:
                    # If a company exists, create a regular employee
                    user = form.save(commit=False)
                    user.role = 'employee'
                    user.company = Company.objects.first()
                    user.save()
                    login(request, user)
                    return redirect('dashboard')

            except IntegrityError:
                form.add_error(None, "An account with this username or email already exists.")

    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def submit_expense(request):
    if request.method == 'POST':
        form = ExpenseClaimForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.submitter = request.user
            expense.save()
            # Optional: Redirect to a success page or history view
            return redirect('expense_history')
    else:
        form = ExpenseClaimForm()
    return render(request, 'submit_expense.html', {'form': form})

@login_required
def expense_history(request):
    expenses = ExpenseClaim.objects.filter(submitter=request.user).order_by('-date')
    return render(request, 'expense_history.html', {'expenses': expenses})

@login_required
def manager_dashboard(request):
    if request.user.role == 'manager' or request.user.role == 'admin':
        pending_expenses = ExpenseClaim.objects.filter(status='pending', submitter__manager=request.user).order_by('date')
        return render(request, 'manager_dashboard.html', {'pending_expenses': pending_expenses})
    else:
        return HttpResponseForbidden("You do not have permission to view this page.")

@login_required
def approve_expense(request, expense_id):
    if request.user.role != 'manager' and request.user.role != 'admin':
        return HttpResponseForbidden("You do not have permission to perform this action.")
    
    expense = get_object_or_404(ExpenseClaim, pk=expense_id)
    
    # Check if the expense is pending approval by this manager
    if expense.status == 'pending' and expense.submitter.manager == request.user:
        # Simple approval logic for now
        expense.status = 'approved'
        expense.save()
        
        # In a real app, this is where you'd update the ApprovalWorkflow
        # and move to the next approver.
        # For now, we'll just approve it directly.
        
    return redirect('manager_dashboard')

@login_required
def reject_expense(request, expense_id):
    if request.user.role != 'manager' and request.user.role != 'admin':
        return HttpResponseForbidden("You do not have permission to perform this action.")
    
    expense = get_object_or_404(ExpenseClaim, pk=expense_id)
    
    if expense.status == 'pending' and expense.submitter.manager == request.user:
        expense.status = 'rejected'
        expense.save()

    return redirect('manager_dashboard')