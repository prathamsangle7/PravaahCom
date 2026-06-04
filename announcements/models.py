from django.db import models
from django.conf import settings

class Announcement(models.Model):
    AUDIENCE = [('all','All'),('student','Students'),('trainer','Trainers'),('admin','Admin')]
    PRIORITY = [('low','Low'),('medium','Medium'),('high','High')]

    title           = models.CharField(max_length=300)
    message         = models.TextField()
    target_audience = models.CharField(max_length=20, choices=AUDIENCE, default='all')
    priority        = models.CharField(max_length=10, choices=PRIORITY, default='medium')
    expires_at      = models.DateTimeField(null=True, blank=True)
    is_active       = models.BooleanField(default=True)
    created_by      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

