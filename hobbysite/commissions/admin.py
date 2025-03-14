from django.contrib import admin
from .models import Commission

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
