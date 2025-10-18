# blog/admin.py - Enhanced
from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'published_date', 'created_at', 'word_count']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_published']
    date_hierarchy = 'published_date'
    
    def word_count(self, obj):
        return len(obj.content.split())
    word_count.short_description = 'Words'