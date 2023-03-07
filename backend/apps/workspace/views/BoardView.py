from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from apps.workspace.models import *
from apps.workspace.serializers.BoardSerializer import BoardSerializer
from django.shortcuts import get_object_or_404


class GetBoards(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        boards = user.boards.all()
        return boards


class CreateBoard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        board_title = request.data.get('title')
        board_color = request.data.get('color')
        if Board.objects.filter(title=board_title, owner=user).exists():
            return Response({
                "Status": "Fail",
                "Message": 'A board with this title already exists',
            }, status=400)

        board = Board.objects.create(
            title=board_title,
            color=board_color,
            owner=request.user
        )
        return Response({
            "Status": "Ok",
            "Message": "Board created",
            "Board": BoardSerializer(board).data
        })


class UpdateBoard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        previous_board_title = request.data.get('title', None)
        new_board_title = request.data.get('new_title', None)
        new_board_color = request.data.get('new_color', None)
        board = Board.objects.filter(title=previous_board_title, owner=request.user).first()
        if new_board_title is not None:
            board.title = new_board_title
        if new_board_color is not None:
            board.color = new_board_color
        board.save()

        return Response({'Message': ' ok'}, status=200)


class DeleteBoard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        title = request.DATA.get('title')
        board = Board.objects.filter(title=title, owner=request.user)
        if not board.exists():
            return Response({'Message': 'there is no board with this title'}, status=404)
        board.delete()
        return Response({'Message': 'board deleted'})


class JoinBoard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, token):
        join_request = get_object_or_404(JoinRequest, token=token)
        board = join_request.board
        board.users.add(request.user)
        return Response({'Message': 'joined to board'})


class InviteToBoard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        board_title = request.data.get("title")
        user_id = request.data.get("user_id")
        board = Board.objects.filter(title=board_title, owner=request.user)
        if not board.exists():
            return Response({"message": "Board does not exist"}, status=404)
        user = User.objects.get(pk=user_id)
        join_request = JoinRequest.objects.create(
            board=board,
            user=user
        )
        return Response({"token": join_request.token})
