from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(this):
		return this.name

class Snapsvisa(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, default=1)
	pre = models.CharField(max_length=256, blank=True)
	lyrics = models.TextField()
	post = models.CharField(max_length=256, blank=True)
	date_updated = models.DateField(auto_now=True)
	date_uploaded = models.DateField(auto_now_add=True)
	protected = models.BooleanField(default=False)

	def __str__(this):
		return this.name