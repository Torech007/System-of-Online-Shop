from django.contrib import admin
from .models import catalog

@admin.register(catalog)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',) 
    list_filter = ('created_at',)