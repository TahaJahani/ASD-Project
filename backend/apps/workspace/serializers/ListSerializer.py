from rest_framework import serializers

from apps.workspace.models import List
from . import CardSerializer


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'title', 'order']


class ListDetailSerializer(serializers.ModelSerializer):
    cards = CardSerializer(source='card_set', many=True)

    class Meta:
        model = List
        fields = ['id', 'title', 'order', 'cards']
