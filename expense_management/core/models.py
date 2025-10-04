# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')

    # Add these lines to prevent clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="core_user_set",
        related_query_name="core_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="core_user_set",
        related_query_name="core_user",
    )
class Company(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=5)

    def __str__(self):
        return self.name


# core/models.py
# ... (add these to the same file)

class ExpenseClaim(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5)
    category = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.submitter.username}'s {self.category} expense"

class ApprovalWorkflow(models.Model):
    expense = models.OneToOneField(ExpenseClaim, on_delete=models.CASCADE, related_name='workflow')
    approvers = models.ManyToManyField(User, related_name='approval_workflows', blank=True)
    sequence = models.TextField(default="[]") # Use TextField for SQLite compatibility

    percentage_rule = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    specific_approver_rule = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='specific_rule_workflows')

    def __str__(self):
        return f"Workflow for {self.expense}"