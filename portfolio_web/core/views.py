from django.shortcuts import render
from projects.models import Project
from blog.models import BlogPost
from .models import Skill

def home(request):
    featured_projects = Project.objects.filter(is_published=True).order_by('-created_at')[:3]
    recent_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')[:3]
    skills = Skill.objects.all().order_by('category', 'display_order')
    
    context = {
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
        'skills': skills,
    }
    return render(request, 'core/home.html', context)

def about(request):
    skills = Skill.objects.all().order_by('category', 'display_order')
    return render(request, 'core/about.html', {'skills': skills})

def skills(request):
    skills = Skill.objects.all().order_by('category', 'display_order')
    return render(request, 'core/skills.html', {'skills': skills})

def contact(request):
    return render(request, 'core/contact.html')