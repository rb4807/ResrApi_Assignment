from django.db import models

"""
    created_on = Recipe created date
"""

class Recipe(models.Model):

    CATEGORY_CHOICES = (
        ('vegetarian', 'Vegetarian'),
        ('non_vegetarian', 'Non-Vegetarian'),
    )

    TYPE_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('juices', 'Juices'),
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    )

    dish = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150, null=True)
    recipe = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dish') 
    ingredients = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    meal_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.dish
    
