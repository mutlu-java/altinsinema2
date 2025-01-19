
 
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Screenwriter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.name

class ProductionCompany(models.Model):
    name = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200, blank=True)
    original_title = models.CharField(max_length=200)
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    release_year = models.IntegerField(default=2000)
    description = models.TextField(default="No description available")
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    iframe_url = models.TextField(default="<iframe></iframe>")
    duration = models.IntegerField(default=0)
    # Relationships
    categories = models.ManyToManyField('Category', related_name="movies")
    directors = models.ManyToManyField('Director', related_name="movies")
    screenwriters = models.ManyToManyField('Screenwriter', related_name="movies")
    actors = models.ManyToManyField('Actor', related_name="movies", blank=True)
    countries = models.ManyToManyField('Country', related_name="movies", blank=True)
    production_companies = models.ManyToManyField('ProductionCompany', related_name="movies", blank=True)

    def __str__(self):
        return self.original_title

# class Movie(models.Model):
#     title = models.CharField(max_length=200, blank=True)
#     original_title = models.CharField(max_length=200)
#     imdb_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
#     release_year = models.IntegerField(default=2000)
#     description = models.TextField(default="No description available")
#     image = models.ImageField(upload_to='movie_images/', default='movie_images/default.jpg')
#     iframe_url = models.TextField(default="<iframe></iframe>")
#     duration = models.IntegerField(default=0)  # Duration in minutes
#     categories = models.ManyToManyField(Category, related_name="movies")
#     directors = models.ManyToManyField(Director, related_name="movies")
#     screenwriters = models.ManyToManyField(Screenwriter, related_name="movies")
#     actors = models.ManyToManyField(Actor, related_name="movies",blank=True)
#     countries = models.ManyToManyField(Country, related_name="movies",blank=True)
#     production_companies = models.ManyToManyField(ProductionCompany, related_name="movies", blank=True)

#     def __str__(self):
#         return self.original_title
 
 