from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(this):
		return this.name

	def next(this):
		return this

	def prev(this):
		return this

class Snapsvisa(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, default=1)
	pre = models.CharField(max_length=256, blank=True)
	lyrics = models.TextField()
	post = models.CharField(max_length=256, blank=True)
	date_updated = models.DateTimeField(auto_now=True)
	date_uploaded = models.DateTimeField(auto_now_add=True)
	protected = models.BooleanField(default=False)

	def __str__(this):
		return this.name