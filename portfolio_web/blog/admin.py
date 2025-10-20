# blog/admin.py - Enhanced
from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'published_date', 'is_published', 'image_preview')
	readonly_fields = ('image_preview',)
	fields = ('title', 'slug', 'excerpt', 'content', 'featured_image', 'image_preview', 'published_date', 'is_published')
	def image_preview(self, obj):
		if obj.featured_image:
			return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', obj.featured_image.url)
		return "No image"
	image_preview.short_description = 'Image Preview'

admin.site.register(BlogPost, BlogPostAdmin)
