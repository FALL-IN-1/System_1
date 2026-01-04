from django.contrib import admin
from .models import Customer
# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ['name','phone']


