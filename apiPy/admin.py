from django.contrib import admin

from .models import UserDetails, UserValuationDetails 

admin.site.register(UserDetails)
admin.site.register(UserValuationDetails)