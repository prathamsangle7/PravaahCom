
from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    PRIORITY_CHOICES = [('low', 'Low'), ('normal', 'Normal'), ('high', 'High')]
    AUDIENCE_CHOICES = [('all', 'All'), ('students', 'Students'), ('trainers', 'Trainers'), ('hostel', 'Hostel')]

    title           = models.CharField(max_length=200)
    message         = models.TextField()
    target_audience = models.CharField(max_length=100, choices=AUDIENCE_CHOICES, default='all')
    priority        = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='normal')
    expires_at      = models.DateTimeField(null=True, blank=True)
    created_by      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    title           = models.CharField(max_length=200)
    file_type       = models.CharField(max_length=50, blank=True)
    file            = models.FileField(upload_to='documents/')
    file_size_kb    = models.IntegerField(null=True, blank=True)
    related_module  = models.CharField(max_length=50, null=True, blank=True)
    related_id      = models.IntegerField(null=True, blank=True)
    download_count  = models.IntegerField(default=0)
    uploaded_by     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title# Create your models here.
