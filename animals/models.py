from django.db import models

# Create your models here.
class Animals(models.Model):
	name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)