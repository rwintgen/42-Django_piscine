from django.db import models

# Create your models here.
class Planets(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True, null=False)
	climate = models.CharField(max_length=128, null=True)
	diameter = models.IntegerField(null=True)
	orbital_period = models.IntegerField(null=True)
	population = models.BigIntegerField(null=True)
	rotation_period = models.IntegerField(null=True)
	surface_water = models.FloatField(null=True)
	terrain = models.CharField(max_length=128, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

class People(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True, null=False)
	birth_year = models.CharField(max_length=32, null=True)
	gender = models.CharField(max_length=32, null=True)
	eye_color = models.CharField(max_length=32, null=True)
	hair_color = models.CharField(max_length=32, null=True)
	height = models.IntegerField(null=True)
	mass = models.FloatField(null=True)
	homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name
	
class Movies(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=128, unique=True, null=False)
	episode_nb = models.IntegerField(unique=True, null=True)
	opening_crawl = models.TextField(null=True)
	director = models.CharField(max_length=64, null=True)
	producer = models.CharField(max_length=128, null=True)
	release_date = models.DateField(null=True)
	characters = models.ManyToManyField(People, related_name="movies")

	def __str__(self):
		return self.title