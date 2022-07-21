from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('user',)

    
    def validate(self, attrs):
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs

    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = instance.user.email
        return rep
