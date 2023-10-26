from rest_framework import serializers
from .models import Ace

class AceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ace
        fields = '__all__'