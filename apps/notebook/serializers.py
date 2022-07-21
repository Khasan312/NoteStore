from apps.notebook.models import NoteBook
from rest_framework import serializers

class NoteBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteBook
        fields = '__all__'


class PurposeSerializer(serializers.Serializer):
    purpose = serializers.CharField(max_length=150)