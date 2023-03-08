from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.workspace.models import *
from apps.workspace.serializers import ListSerializer, ListDetailSerializer


class ListLists(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListDetailSerializer

    def get_queryset(self):
        board_id = self.request.GET.get('board_id')
        user = self.request.user
        lists = List.objects.filter(board_id=board_id, board__users__in=[user]).all()
        return lists


class CreateList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        board_id = request.data.get('board_id')
        title = request.data.get('title')
        board = get_object_or_404(Board, pk=board_id)
        list_order = List.objects.filter(board=board).count()
        list_obj = List.objects.create(
            board=board,
            title=title,
            order=list_order
        )
        return Response(ListSerializer(list_obj))


class UpdateList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        list_id = request.data.get('list_id')
        title = request.data.get('title')

        List.objects.filter(pk=list_id, board__users__in=[request.user]).update(
            title=title
        )

        return Response({"message": "List updated"})


class DeleteList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        List.objects.filter(pk=pk, board__users__in=[request.user]).delete()
        return Response({"message": "List deleted"})
