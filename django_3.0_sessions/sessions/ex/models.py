from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

# Create your models here.
class CustomUser(AbstractUser):
	reputation = models.IntegerField(default=0)

	def update_reputation(self):
		upvotes = 0
		downvotes = 0

		for tip in Tip.objects.filter(author=self):
			upvotes += tip.upvotes_count()
			downvotes += tip.downvotes_count()
		
		self.reputation = upvotes * 5 - downvotes * 2
		self.save()

		can_downvote_perm = Permission.objects.get(codename="can_downvote_tip")
		can_delete_perm = Permission.objects.get(codename="delete_tip")

		if self.reputation >= 15:
			self.user_permissions.add(can_downvote_perm)
		else:
			self.user_permissions.remove(can_downvote_perm)

		if self.reputation >= 30:
			self.user_permissions.add(can_delete_perm)
		else:
			self.user_permissions.remove(can_delete_perm)

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
	
	class Meta:
		permissions = [
			("can_downvote_tip", "Can downvote tip")
		]
