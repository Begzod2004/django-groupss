from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Position

class PositionSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Position)
    
    class Meta:
        model = Position
        fields = '__all__'