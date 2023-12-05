from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'image']
    list_display_links = ['title']
    search_fields = ['title']
