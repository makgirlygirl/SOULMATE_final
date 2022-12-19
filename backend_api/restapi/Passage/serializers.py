from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Passage

class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = '__all__'