from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publication(models.Model):
	title = models.CharField(max_length=150)
	body = models.CharField(max_length=150)
	creation_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "Publication"
		verbose_name_plural = "Publications"
	def __str__(self):
		return self.title