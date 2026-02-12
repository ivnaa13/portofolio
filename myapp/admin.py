# main/admin.py

from django.contrib import admin
from .models import (
    Project, ProjectImage, ProjectCertificate, 
    ContactMessage, ToolImage, AboutPage, Interest, Skill
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3
    fields = ('image', 'caption', 'order')

class ProjectCertificateInline(admin.TabularInline):
    model = ProjectCertificate
    extra = 1
    fields = ('title', 'issuer', 'issue_date', 'certificate_image', 'certificate_file', 'credential_url')

class ToolImageInline(admin.TabularInline):
    model = ToolImage
    extra = 2
    fields = ('tool_name', 'tool_image', 'order')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'role', 'start_date', 'end_date', 'created_at', 'is_featured')
    list_filter = ('is_featured', 'category', 'created_at', 'start_date')
    search_fields = ('title', 'description', 'tech_stack', 'category')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline, ProjectCertificateInline, ToolImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'role', 'image', 'is_featured')
        }),
        ('Technical Details', {
            'fields': ('tech_stack', 'skills_used', 'tools_used')
        }),
        ('Project Details', {
            'fields': ('category', 'start_date', 'end_date')
        }),
        ('Links', {
            'fields': ('github_link', 'demo_link')
        }),
    )

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'order', 'uploaded_at')
    list_filter = ('project', 'uploaded_at')
    search_fields = ('project__title', 'caption')

@admin.register(ProjectCertificate)
class ProjectCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'issuer', 'issue_date')
    list_filter = ('project', 'issuer', 'issue_date')
    search_fields = ('title', 'project__title', 'issuer')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)

@admin.register(ToolImage)
class ToolImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'tool_name', 'order')
    list_filter = ('project',)
    search_fields = ('tool_name', 'project__title')
    ordering = ('project', 'order')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'year', 'gpa', 'updated_at')
    readonly_fields = ('updated_at',)
    
    def has_add_permission(self, request):
        # Hanya boleh ada 1 instance
        return not AboutPage.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Tidak bisa dihapus
        return False

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('order',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order', 'is_active')
    list_filter = ('category', 'proficiency', 'is_active')
    search_fields = ('name',)
    ordering = ('category', 'order', 'name')
    list_editable = ('order', 'is_active')
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'image', 'proficiency')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )