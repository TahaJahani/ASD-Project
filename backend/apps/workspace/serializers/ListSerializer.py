from rest_framework import serializers

from apps.workspace.models import CardsList
from . import CardSerializer


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardsList
        fields = ['id', 'title', 'order']


class ListDetailSerializer(serializers.ModelSerializer):
    cards = CardSerializer(source='card_set', many=True)

    class Meta:
        model = CardsList
        fields = ['id', 'title', 'order', 'cards']
