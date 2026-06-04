from django.db import models
from django.contrib.auth.models import User


# Minimal Trainer model used by calendar_module and other apps.
class Trainer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=30, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		if self.user:
			return getattr(self.user, 'username', str(self.user))
		name = f"{self.first_name} {self.last_name}".strip()
		return name or self.email or f"Trainer {self.id}"
