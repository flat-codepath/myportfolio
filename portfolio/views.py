from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Profile, Education, Skill, Experience, Project, Achievement

def portfolio(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'education': education,
        'skills_by_category': skills_by_category,
        'experiences': experiences,
        'projects': projects,
        'achievements': achievements,
    }
    
    return render(request, 'index3.html', context)