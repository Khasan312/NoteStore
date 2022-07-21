from rest_framework import serializers

from apps.accessories.models import Bag


class ThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = '__all__'