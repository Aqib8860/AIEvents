from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_superuser', 'is_customer', 'subscribed']
    list_filter = ['is_customer', 'subscribed']
