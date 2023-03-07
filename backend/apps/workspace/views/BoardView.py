from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from apps.workspace.models import *


class CreateBoard(APIView):
    authentication_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        board_title = request.POST.get('title')
        board_color = request.POST('color')
        privacy = request.POST.get('privacy')
        if Board.objects.filter(title=board_title, owner=user).exists():
            return Response({
                "Status": "Fail",
                "Message": 'A board with this title already exists',
            }, status=400)

        board = Board(title=board_title, color=board_color, privacy=privacy)
        board.save()
        return Response({
            "Status": "Ok",
            "Message": "Board created",
            "Board": board.to_dict()
        })


class UpdateBoard(APIView):
    authentication_classes = [IsAuthenticated]

    def post(self, request):
        previous_board_title = request.POST.get('title', None)
        new_board_title = request.POST.get('new_title', None)
        new_board_color = request.POST.get('new_color', None)
        board = Board.objects.filter(title=previous_board_title, owner=request.user).first()
        if new_board_title is not None:
            board.title = new_board_title
        if new_board_color is not None:
            board.color = new_board_color
        board.save()

        return Response({'Message': ' ok'}, status=200)
