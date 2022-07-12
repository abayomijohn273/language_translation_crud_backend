from rest_framework import serializers
from translatorcrud.models import TranslationsModel

class TranslationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranslationsModel
        fields="__all__"