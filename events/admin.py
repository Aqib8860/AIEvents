from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'category', 'entry_type', 'date', 'add_date']
    list_filter = ['category', 'entry_type']
