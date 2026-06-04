
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class CalendarEvent(models.Model):
    EVENT_TYPES = [
        ('session',     'Session'),
        ('exam',        'Exam'),
        ('holiday',     'Holiday'),
        ('unavailable', 'Unavailable'),
        ('hostel',      'Hostel'),
        ('other',       'Other'),
    ]

    title          = models.CharField(max_length=200)
    description    = models.TextField(blank=True)
    event_type     = models.CharField(max_length=20, choices=EVENT_TYPES)
    start_datetime = models.DateTimeField()
    end_datetime   = models.DateTimeField()
    all_day        = models.BooleanField(default=False)
    related_module = models.CharField(max_length=50, blank=True)
    related_id     = models.IntegerField(null=True, blank=True)
    created_by     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TrainerUnavailability(models.Model):
    trainer    = models.ForeignKey('trainers.Trainer', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date   = models.DateField()
    reason     = models.CharField(max_length=255, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trainer} | {self.start_date} to {self.end_date}"

    def conflicts_with(self, check_date):
        return self.start_date <= check_date <= self.end_date and self.is_approved