from django.db import models
from django.conf import settings

class Document(models.Model):
	title           = models.CharField(max_length=200)
	file_type       = models.CharField(max_length=50, blank=True)
	file            = models.FileField(upload_to='documents/')
	file_size_kb    = models.IntegerField(null=True, blank=True)
	related_module  = models.CharField(max_length=50, null=True, blank=True)
	related_id      = models.IntegerField(null=True, blank=True)
	download_count  = models.IntegerField(default=0)
	uploaded_by     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	uploaded_at     = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
