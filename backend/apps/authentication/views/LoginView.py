from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginView(APIView):
    http_method_names = ['post']

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                token = Token.objects.filter(user=user)
                if token.exists():
                    token = token.get()
                else:
                    token = Token.objects.create(user=user)
                return Response(data={
                    "token": token.key
                })
            raise Exception()
        except:
            return Response(data={
                "error": "wrong username or password"
            }, status=403)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({"message": "Logged out successfully"})
