# main/models.py

from django.db import models

class Project(models.Model):
    """Model untuk menyimpan project portfolio"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated tech stack")
    skills_used = models.TextField(help_text="Skills yang digunakan dalam project")
    tools_used = models.TextField(help_text="Tools yang digunakan dalam project")
    role = models.CharField(max_length=200, help_text="Peran Anda dalam project ini")
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tech_stack_list(self):
        """Return tech stack as a list"""
        return [tech.strip() for tech in self.tech_stack.split(',')]
    
    def get_skills_list(self):
        """Return skills as a list"""
        return [skill.strip() for skill in self.skills_used.split(',')]
    
    def get_tools_list(self):
        """Return tools as a list"""
        return [tool.strip() for tool in self.tools_used.split(',')]


class ContactMessage(models.Model):
    """Model untuk menyimpan pesan dari contact form"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"