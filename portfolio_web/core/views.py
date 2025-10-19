from django.shortcuts import render
from projects.models import Project
from blog.models import BlogPost
from .models import Skill
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_submission = form.save()
            
            # Send email notification
            send_mail(
                f"Portfolio Contact: {form.cleaned_data['subject']}",
                f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # Reset form
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})