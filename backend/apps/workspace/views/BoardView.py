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
