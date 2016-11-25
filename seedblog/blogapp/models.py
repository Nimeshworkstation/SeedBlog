from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class BlogPost(models.Model):
	author = models.ForeignKey('auth.user', blank = True, null = True)
	title =  models.CharField(max_length=200)
	content = models.TextField()
	def __str__(self):
		return self.title
	created = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updated = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	publish = models.BooleanField(default = False)