from rest_framework.serializers import ModelSerializer

from .models import Track


class TrackModelSerializer(ModelSerializer):
    
    class Meta:
        model=Track
        fields='__all__'