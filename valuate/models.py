from django.db import models

class UserValuationDetails(models.Model):
    size = models.CharField(max_length=50)
    land_type = models.CharField(max_length=50)
    distance_to_town = models.CharField(max_length=50)
    calculate_year = models.CharField(max_length=4)
    lane = models.CharField(max_length=50)
    predicted_value = models.CharField(max_length=50)
