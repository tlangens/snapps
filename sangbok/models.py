from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(this):
		return this.name

class Snapsvisa(models.Model):
	name = models.CharField(max_length=100)
	other = models.CharField(max_length=256, blank=True)
	category = models.ForeignKey(Category, default=1)
	lyrics = models.TextField()
	date_updated = models.DateField(auto_now=True)
	date_uploaded = models.DateField(auto_now_add=True)

	def __str__(this):
		return this.name