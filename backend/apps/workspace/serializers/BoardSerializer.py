from rest_framework import serializers

from apps.workspace.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'color']
