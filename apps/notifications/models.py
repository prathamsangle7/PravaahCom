from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    TYPE_CHOICES = [
        ('email', 'Email'),
        ('system', 'System'),
        ('sms', 'SMS'),
    ]

    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title      = models.CharField(max_length=200)
    message    = models.TextField()
    type       = models.CharField(max_length=20, choices=TYPE_CHOICES, default='system')
    is_read    = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)
    read_at    = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} — {self.title}"


class EmailLog(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]

    recipient    = models.EmailField()
    subject      = models.CharField(max_length=255)
    body_preview = models.TextField(blank=True)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    error_msg    = models.TextField(null=True, blank=True)
    sent_by      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sent_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient} — {self.status}"


class NotificationPreference(models.Model):
    user             = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notification_preference')
    email_on         = models.BooleanField(default=True)
    system_on        = models.BooleanField(default=True)
    enrollment_notif = models.BooleanField(default=True)
    fee_reminder     = models.BooleanField(default=True)
    result_notif     = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferences — {self.user}"