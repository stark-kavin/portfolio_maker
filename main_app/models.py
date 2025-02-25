from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
    full_name = models.CharField(max_length=50)
    socials = models.JSONField(default=dict)
    about_me = models.TextField()
    title = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    roles = models.JSONField(default=list)
    skills = models.JSONField(default=dict)
    education = models.JSONField(default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.id}"
