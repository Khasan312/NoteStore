from rest_framework import serializers


class HelpSerializer(serializers.Serializer):
    help = serializers.CharField(max_length=300)


class AboutUsSerializer(serializers.Serializer):
    about_us = serializers.CharField(max_length=500)