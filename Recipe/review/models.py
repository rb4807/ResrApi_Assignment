from django.db import models
from crud.models import Recipe
from django.contrib.auth.models import User

"""
    created_on = Recipe created date
"""

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )
    
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

