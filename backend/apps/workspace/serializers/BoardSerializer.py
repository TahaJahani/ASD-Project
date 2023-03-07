from rest_framework import serializers

from apps.workspace.models import Board
from apps.workspace.serializers import ListDetailSerializer


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'color']


class BoardDetailSerializer(serializers.ModelSerializer):
    lists = ListDetailSerializer(source='list_set')

    class Meta:
        model = Board
        fields = ['id', 'title', 'color', 'lists']
