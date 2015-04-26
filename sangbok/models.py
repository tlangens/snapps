from django.db import models
class OrderManager(models.Manager):
	# These are not so efficient. Perhaps there is a better way?
	def next(self, cur):
		s = super(OrderManager, self).all()
		first = None
		found = False
		for i in s:
			if found:
				return i
			if i == cur:
				found = True
			if not first:
				first = i
		return first

	def prev(self, cur):
		s = super(OrderManager, self).all()
		prev = None
		for i in s:
			if i == cur:
				if prev:
					return prev
			prev = i
		return prev

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
	date_updated = models.DateTimeField(auto_now=True)
	date_uploaded = models.DateTimeField(auto_now_add=True)
	protected = models.BooleanField(default=False)
	objects = OrderManager()

	def __str__(this):
		return this.name

	class Meta:
		ordering = ['category', 'date_uploaded']