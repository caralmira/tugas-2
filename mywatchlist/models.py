from django.db import models

class MyWatchlist(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
    
# https://www.geeksforgeeks.org/datefield-django-models/