from django.test import TestCase
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your tests here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True)
    career_objective = models.TextField()
    personal_profile = models.TextField(blank=True)
    gender = models.CharField(max_length=10, blank=True)
    dob = models.DateField(blank=True, null=True)
    languages = models.TextField(blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    profile_photo=models.ImageField( upload_to='media/profiles',blank=True, null=True)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    period = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order']
    
    def __str__(self):
        return self.degree

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('web', 'Web Frameworks & Libraries'),
        ('real_time', 'Real-time Tech'),
        ('architecture', 'Architecture & Design'),
        ('databases', 'Databases'),
        ('version_control', 'Version Control'),
        ('tools', 'Tools & Services'),
        ('others', 'Others'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    period = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    features = models.TextField(blank=True)
    is_professional = models.BooleanField(default=False)
    github_link = models.URLField(max_length=200,blank=True,help_text="GitHub project link")
    live_link = models.URLField(max_length=200,blank=True,help_text="Live project link")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-is_professional', '-order']
    
    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order']
    
    def __str__(self):
        return self.title