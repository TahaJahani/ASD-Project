import datetime

from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.workspace.models import *
from apps.workspace.serializers.CardSerializer import CardSerializer


class ListCards(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer

    def get_queryset(self):
        list_id = self.request.GET.get('list_id')
        user = self.request.user
        cards = Card.objects.filter(list_id=list_id, list__board__users__in=[user]).all()
        return cards


class CreateCard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        list_id = request.data.get('list_id')
        related_list = CardsList.objects.filter(pk=list_id, board__users__in=[request.user])
        related_list = get_object_or_404(related_list)
        card_title = request.data.get('title')
        card_order = Card.objects.filter(list=related_list).count()
        card = Card.objects.create(
            card_list=related_list,
            order=card_order,
            title=card_title,
            due_date=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        return Response(CardSerializer(card).data)


class UpdateCard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        description = request.data.get('description', None)
        title = request.data.get('title', None)
        card_id = request.data.get('card_id')

        card = Card.objects.filter(pk=card_id, list__board__users__in=[request.user])
        card = get_object_or_404(card)

        if title is not None:
            card.title = title
        if description is not None:
            card.description = description
        card.save()
        return Response({'Message': 'card updated'})


class DeleteCard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        Card.objects.filter(pk=pk, list__board__users__in=[request.user]).delete()
        return Response({'Message': 'card deleted'})
