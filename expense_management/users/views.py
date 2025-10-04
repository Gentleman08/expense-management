from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomLoginForm

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
# Create your views here.
