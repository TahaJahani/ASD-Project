from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    http_method_names = ['get']

    def get(self, request):
        return Response(data={
            "message": "Route Is Working Just Fine!, Edited!"
        })