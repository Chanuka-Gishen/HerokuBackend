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
            'lane',
            'predicted_value'
        )
        