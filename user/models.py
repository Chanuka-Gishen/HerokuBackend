from django.db import models

class UserDetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_mobileNo = models.CharField(max_length=50)
