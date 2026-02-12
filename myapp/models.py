# main/models.py

from django.db import models

class Project(models.Model):
    """Model untuk menyimpan project portfolio"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated tech stack")
    skills_used = models.TextField(help_text="Skills yang digunakan dalam project")
    tools_used = models.TextField(help_text="Tools yang digunakan dalam project")
    role = models.CharField(max_length=200, help_text="Peran Anda dalam project ini")
    category = models.CharField(max_length=100, blank=True, help_text="Kategori project")
    start_date = models.DateField(blank=True, null=True, help_text="Tanggal mulai project")
    end_date = models.DateField(blank=True, null=True, help_text="Tanggal selesai project")
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Featured/Thumbnail image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, help_text="Tampilkan di homepage")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tech_stack_list(self):
        """Return tech stack as a list"""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]
    
    def get_skills_list(self):
        """Return skills as a list"""
        return [skill.strip() for skill in self.skills_used.split(',') if skill.strip()]
    
    def get_tools_list(self):
        """Return tools as a list"""
        return [tool.strip() for tool in self.tools_used.split(',') if tool.strip()]


class ProjectImage(models.Model):
    """Model untuk menyimpan multiple images per project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0, help_text="Urutan tampilan gambar")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'uploaded_at']
    
    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class ProjectCertificate(models.Model):
    """Model untuk menyimpan sertifikat terkait project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200, help_text="Nama sertifikat")
    issuer = models.CharField(max_length=200, help_text="Pemberi sertifikat")
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_image = models.ImageField(upload_to='certificate_images/', blank=True, null=True)
    credential_url = models.URLField(blank=True, help_text="Link verifikasi sertifikat")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"{self.title} - {self.project.title}"


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


class ToolImage(models.Model):
    """Model untuk menyimpan gambar tools yang digunakan dalam project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tool_images')
    tool_name = models.CharField(max_length=100, help_text="Nama tool/teknologi")
    tool_image = models.ImageField(upload_to='tool_images/', help_text="Logo/icon tool")
    order = models.IntegerField(default=0, help_text="Urutan tampilan")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'tool_name']
        verbose_name = "Tool Image"
        verbose_name_plural = "Tool Images"
    
    def __str__(self):
        return f"{self.project.title} - {self.tool_name}"


class AboutPage(models.Model):
    """Model untuk menyimpan informasi About Page"""
    picture = models.ImageField(upload_to='about/', help_text="Foto profil untuk halaman About")
    degree = models.CharField(max_length=200, default="Bachelor of Information Systems")
    university = models.CharField(max_length=200, default="Universitas Komputer Indonesia")
    year = models.CharField(max_length=100, default="2021 - Present")
    gpa = models.CharField(max_length=20, default="3.62/4.00")
    transcript = models.FileField(upload_to='documents/', help_text="Upload transcript PDF", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
    
    def __str__(self):
        return "About Page Settings"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and AboutPage.objects.exists():
            raise ValueError('Only one AboutPage instance is allowed')
        return super(AboutPage, self).save(*args, **kwargs)


class Interest(models.Model):
    """Model untuk menyimpan areas of interest"""
    title = models.CharField(max_length=200, help_text="Nama area of interest")
    order = models.IntegerField(default=0, help_text="Urutan tampilan")
    is_active = models.BooleanField(default=True, help_text="Tampilkan di halaman About")
    
    class Meta:
        ordering = ['order']
        verbose_name = "Area of Interest"
        verbose_name_plural = "Areas of Interest"
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    """Model untuk menyimpan technical skills dan tools"""
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('tool', 'Tools & Platforms'),
        ('ml', 'Machine Learning & AI'),
        ('visualization', 'Data Visualization'),
        ('other', 'Other'),
    ]
    
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100, help_text="Nama skill/tool")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', help_text="Kategori skill")
    image = models.ImageField(upload_to='skills/', help_text="Logo/icon skill")
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, blank=True, help_text="Tingkat kemahiran")
    order = models.IntegerField(default=0, help_text="Urutan tampilan dalam kategori")
    is_active = models.BooleanField(default=True, help_text="Tampilkan di halaman About")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"