from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Ensure this import path is correct for your project structure
from .models import CustomUser 


# --- 1. Custom Login Form ---
class CustomLoginForm(AuthenticationForm):
    """
    Customizes the login form by adding placeholders for better UX, 
    matching the dark-mode HTML design.
    """
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username or email',
            'class': 'form-input' # Custom class for styling in HTML
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-input' # Custom class for styling in HTML
        })
    )

# --- 2. User Registration Form ---
class UserRegistrationForm(UserCreationForm):
    """
    Extends UserCreationForm to include first_name, last_name, email, 
    phone_number, organization_name, and the role choice field.
    """
    # Fields inherited from AbstractUser (defined here for widget/label control)
    first_name = forms.CharField(
        label='First Name',
        max_length=150,
        required=True
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=150,
        required=True
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'user@example.com'}),
        label='Email Address'
    )
    
    # Custom fields now present on CustomUser model
    phone_number = forms.CharField(
        label='Phone Number (Optional)',
        max_length=15,
        required=False,
    )
    organization_name = forms.CharField(
        label='Project/Organization Name',
        max_length=100,
        required=True,
    )

    # Existing Role Field
    ROLE_CHOICES = (
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        # Include all custom fields (must match fields defined in CustomUser model)
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'organization_name', 
            'role'
        ]
        
    # Override save method to set all custom fields on the CustomUser instance
    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Set all custom fields using the data cleaned by the form
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.organization_name = self.cleaned_data["organization_name"]
        user.role = self.cleaned_data["role"]

        if commit:
            user.save()
        return user
