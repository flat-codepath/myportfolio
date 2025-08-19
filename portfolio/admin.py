from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Education, Skill, Experience, Project, Achievement

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'nationality')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'linkedin')
        }),
        ('Career Information', {
            'fields': ('career_objective',)
        }),
        ('Personal Details', {
            'fields': ('personal_profile', 'gender', 'dob', 'languages', 'nationality','profile_photo')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'period', 'score', 'order')
    list_editable = ('order',)
    list_filter = ('institution',)
    search_fields = ('degree', 'institution')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_editable = ('category', 'order')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'period', 'order')
    list_editable = ('order',)
    list_filter = ('company',)
    search_fields = ('position', 'company', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'is_professional', 'order')
    list_editable = ('is_professional', 'order')
    list_filter = ('is_professional',)
    search_fields = ('title', 'technologies', 'description')
    filter_horizontal = ()

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date', 'order')
    list_editable = ('order',)
    list_filter = ('issuer', 'date')
    search_fields = ('title', 'issuer', 'description')

# Optional: Customize the admin site header and title
admin.site.site_header = "Nagnath Portfolio Administration"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"