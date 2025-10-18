from django.db import models


class Skill(models.Model):
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=100, blank=True)
	display_order = models.PositiveIntegerField(default=0)
	description = models.TextField(blank=True)

	class Meta:
		ordering = ['category', 'display_order']

	def __str__(self):
		return self.name
