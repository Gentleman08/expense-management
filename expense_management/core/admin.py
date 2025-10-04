# core/admin.py
from django.contrib import admin
from .models import User, Company, ExpenseClaim, ApprovalWorkflow

admin.site.register(User)
admin.site.register(Company)
admin.site.register(ExpenseClaim)
admin.site.register(ApprovalWorkflow)