from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikesSerializer(serializers.ModelSerializer):
    """
    Docstring
    """
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Like
        fields = [
            'id', 'created_at', 'owner', 'post'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'warning: possible duplicate'
            })