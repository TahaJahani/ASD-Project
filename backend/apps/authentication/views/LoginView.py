from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..forms import LoginForm


class LoginView(APIView):
    http_method_names = ['post']

    def post(self, request):
        login_form = LoginForm(request.data)
        if not login_form.is_valid():
            return Response(data=login_form.errors)

        email = request.data["email"]
        password = request.data["password"]
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                token = Token.objects.create(user=user)
                return Response(data={
                    "token": token.key
                })
        except:
            return Response(data={
                "error": "wrong username or password"
            }, status=403)


class LogoutView(APIView):
    authentication_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({"message": "Logged out successfully"})
