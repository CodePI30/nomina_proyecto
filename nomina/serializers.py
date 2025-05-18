from rest_framework import serializers
from .models import Nomina

class NominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = '__all__'
