from django.urls import path
from . import views
from .views import UserLoginView # Import the class-based view

urlpatterns = [
    # path is: /users/register/ (when combined with project-level urls)
    path('register/', views.register, name='register'),
    
    # path is: /users/login/ (when combined with project-level urls)
    path('login/', UserLoginView.as_view(), name='login'),
    # path('dashboard/', dashboard, name='dashboard'),

]