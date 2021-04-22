from django.db import models

class UserValuationDetails(models.Model):
    size = models.CharField(max_length=50)
    land_type = models.CharField(max_length=50)
    distance_to_town = models.CharField(max_length=50)
    calculate_year = models.CharField(max_length=4)
    lane = models.CharField(max_length=50)
<<<<<<< HEAD
    predicted_value = models.CharField(max_length=50)
=======
<<<<<<< HEAD
    predicted_value = models.CharField(max_length=50)
=======
>>>>>>> 57010dc66c7dfd8b11e12266fe8d17c721db3e6a
>>>>>>> 848a9d980a02ae766012861a4f2106128c8a45c5
