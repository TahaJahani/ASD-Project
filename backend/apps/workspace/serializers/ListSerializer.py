from rest_framework import serializers

from apps.workspace.models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'title', 'order']
