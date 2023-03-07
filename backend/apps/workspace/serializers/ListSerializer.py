from rest_framework import serializers

from apps.workspace.models import List
from apps.workspace.serializers import CardSerializer


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'title', 'order']


class ListDetailSerializer(serializers.ModelSerializer):
    cards = CardSerializer(source='card_set')

    class Meta:
        model = List
        fields = ['id', 'title', 'order', 'cards']
