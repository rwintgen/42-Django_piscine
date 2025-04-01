from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle
from django.utils.translation import activate

# Create your tests here.
class Ex06Tests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='password123')
		self.client.login(username='testuser', password='password123')
		self.article = Article.objects.create(title="Test Article", synopsis="Test Synopsis", content="Test Content")

	def test_views_accessible_by_registered_users_only(self):
		self.client.logout()
		restricted_urls = [
			reverse('favourites'),
			reverse('publications'),
			reverse('publish'),
		]
		for url in restricted_urls:
			response = self.client.get(url)
			self.assertNotEqual(response.status_code, 200)  # Not accessible

		self.client.login(username='testuser', password='password123')
		for url in restricted_urls:
			response = self.client.get(url)
			self.assertEqual(response.status_code, 200)  # Accessible

	def test_registered_user_cannot_access_new_user_creation_form(self):
		response = self.client.get(reverse('register'))
		self.assertNotEqual(response.status_code, 200)  # Accessible

	def test_cannot_add_same_article_twice_to_favourites(self):
		activate('en')
		UserFavouriteArticle.objects.create(user=self.user, article=self.article)
		
		url = reverse('add_favourite', kwargs={'pk': self.article.id})
		response = self.client.post(url, {})
		
		self.assertContains(response, "Article already in favourites.", status_code=200)
		self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)
		