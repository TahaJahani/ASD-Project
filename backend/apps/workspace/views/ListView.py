from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from apps.workspace.models import *
from apps.workspace.serializers import ListSerializer
from apps.workspace.serializers.BoardSerializer import BoardSerializer
from django.shortcuts import get_object_or_404


class ListLists(ListAPIView):
    authentication_classes = [IsAuthenticated]

    def get_queryset(self):
        board_id = self.request.GET.get('board_id')
        user = self.request.user
        lists = List.objects.filter(board_id=board_id, board__users__in=[user]).all()
        return Response(ListSerializer(lists, many=True))
