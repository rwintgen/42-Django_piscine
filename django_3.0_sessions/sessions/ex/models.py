from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
	pass

class Tip(models.Model):
	content = models.TextField()
	author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	date = models.DateTimeField(auto_now_add=True)
	upvotes = models.ManyToManyField(CustomUser, related_name="upvoted_tips", blank=True)
	downvotes = models.ManyToManyField(CustomUser, related_name="downvoted_tips", blank=True)

	def upvotes_count(self):
		return self.upvotes.count()

	def downvotes_count(self):
		return self.downvotes.count()
