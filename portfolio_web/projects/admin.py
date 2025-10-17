# projects/admin.py - Enhanced
from django.contrib import admin
from .models import Project, Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_count']
    search_fields = ['name']
    
    def project_count(self, obj):
        return obj.project_set.count()
    project_count.short_description = 'Projects'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies_list', 'created_at', 'is_published']
    list_filter = ['technologies_used', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['technologies_used']
    list_editable = ['is_published']
    readonly_fields = ['created_at', 'updated_at']
    
    def technologies_list(self, obj):
        return ", ".join([tech.name for tech in obj.technologies_used.all()])
    technologies_list.short_description = 'Technologies'