# main/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, AboutPage, Skill
from .forms import ContactForm

def home(request):
    """Homepage dengan hero section dan featured projects"""
    # Ambil 3 project terbaru untuk featured projects
    featured_projects = Project.objects.all()[:3]
    total_projects = Project.objects.count()
    
    context = {
        'name': 'Nur Ivana Maharani Soamole',
        'role': 'Information Systems Student',
        'summary': 'Currently pursuing a degree in Information Systems with focus on Data Science.',
        'featured_projects': featured_projects,
        'total_projects': total_projects,
    }
    return render(request, 'home.html', context)


def about(request):
    """About page dengan background pendidikan"""
    # Ambil data dari AboutPage model (jika ada)
    about_page = AboutPage.objects.first()
    
    # Ambil semua skills yang aktif
    skills = Skill.objects.filter(is_active=True)
    
    context = {
        'about_page': about_page,
        'skills': skills,
        'education': {
            'degree': 'Bachelor of Information Systems',
            'university': 'President University',
            'year': '2023 - Present',
            'gpa': '3.62/4.0'
        },
        'interests': [
            'Data Science & Analytics',
            'Machine Learning',
            'Web Development',
            'Data Visualization',
        ]
    }
    return render(request, 'about.html', context)


def projects(request):
    """Projects page dengan data dari database"""
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)


def project_detail(request, project_id):
    """Detail page untuk setiap project"""
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project
    }
    return render(request, 'myapp/project_detail.html', context)


def contact(request):
    """Contact page dengan form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('myapp:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'email': 'ivanamaharani11@gemail.com',
        'phone': '+628 211-136-2338',
        'whatsapp_number': '+6282111362338',
        'location': 'Jakarta, Indonesia',
        'linkedin_url': 'https://www.linkedin.com/in/nur-ivana/',
        'github_url': 'https://github.com/ivnaa13',
    }
    return render(request, 'contact.html', context)