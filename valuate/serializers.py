from rest_framework import serializers
from valuate.models import UserValuationDetails

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserValuationDetails
        fields = (
            'size',
            'land_type',
            'distance_to_town',
            'calculate_year',
<<<<<<< HEAD
            'lane',
            'predicted_value'
=======
            'lane'
>>>>>>> 57010dc66c7dfd8b11e12266fe8d17c721db3e6a
        )
        