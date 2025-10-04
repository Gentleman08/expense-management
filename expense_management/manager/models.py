from django.db import models
from django.conf import settings
# Create your models here.
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
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
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
    approvers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='approval_workflows', blank=True)
    sequence = models.TextField(default="[]")  # JSON string of user IDs or usernames

    percentage_rule = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    specific_approver_rule = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='specific_rule_workflows'
    )

    def __str__(self):
        return f"Workflow for {self.expense}"