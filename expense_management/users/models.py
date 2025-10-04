from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
    )
    
    # Existing field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='EMPLOYEE')
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_members')

    # NEW FIELD 1: Phone Number (matches form)
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        help_text='Optional phone number for contact.'
    )
    
    # NEW FIELD 2: Organization/Project Name (matches form)
    organization_name = models.CharField(
        max_length=100, 
        blank=False, 
        null=False,
        default='Default Project' # Add a default or make sure it is provided by the form
    )

    # You must include pass here or add custom methods if desired
    pass 
