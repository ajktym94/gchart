from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Response(models.Model):
	recname=models.CharField(max_length=200)
	reference=models.CharField(max_length=200)
	idf=models.BigIntegerField(default=0)
	state=models.CharField(max_length=200)
	country=models.CharField(max_length=200)
