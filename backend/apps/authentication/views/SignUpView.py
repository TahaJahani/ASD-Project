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
            request.data["email"],
            request.data["password"]
        )
        if "first_name" in request.data:
            user.first_name = request.data["first_name"]
        if "last_name" in request.data:
            user.last_name = request.data["last_name"]
        user.save()
        return Response(data={
            "message": "Saved Successfully",
        })
