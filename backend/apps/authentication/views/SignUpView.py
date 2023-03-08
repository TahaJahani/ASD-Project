from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..forms import SignUpForm
from django.contrib.auth.models import User


class SignUpView(APIView):
    http_method_names = ['post']

    def post(self, request):
        signup_form = SignUpForm(request.data)
        if not signup_form.is_valid():
            return Response(data=signup_form.errors)
        user = User.objects.create_user(
            request.data["username"],
            password=request.data["password"]
        )
        if "email" in request.data:
            user.email = request.data["email"]
        if "first_name" in request.data:
            user.first_name = request.data["first_name"]
        if "last_name" in request.data:
            user.last_name = request.data["last_name"]
        user.save()
        return Response(data={
            "message": "Saved Successfully",
        })


class EditProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        first_name = request.data.get('first_name', user.first_name)
        last_name = request.data.get('last_name', user.last_name)
        email = request.data.get('email', user.email)
        password = request.data.get('password')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password is not None:
            user.set_password(password)
        user.save()
        return Response({"message": "Data updated"})
