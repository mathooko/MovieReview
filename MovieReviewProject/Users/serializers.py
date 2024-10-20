from rest_framework import serializers
from .models import Users

class CohortSerializer(Serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"