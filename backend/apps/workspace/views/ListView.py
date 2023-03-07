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


class CreateList(APIView):
    authentication_classes = [IsAuthenticated]

    def post(self, request):
        board_id = request.POST.get('board_id')
        title = request.POST.get('title')
        board = get_object_or_404(Board, pk=board_id)
        list_order = List.objects.filter(board=board).count()
        list_obj = List.create(
            board=board,
            title=title,
            order=list_order
        )
        return Response(ListSerializer(list_obj))


class UpdateList(APIView):
    authentication_classes = [IsAuthenticated]

    def post(self, request):
        list_id = request.POST.get('list_id')
        title = request.POST.get('title')

        List.objects.filter(pk=list_id, board__users__in=[request.user]).update(
            title=title
        )

        return Response({"message": "List updated"})


class DeleteList(APIView):
    authentication_classes = [IsAuthenticated]

    def delete(self, request, pk):
        List.objects.filter(pk=pk, board__users__in=[request.user]).delete()
        return Response({"message": "List deleted"})
