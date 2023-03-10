from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from ..models import ResetPassword


class RequestResetPassword(APIView):
    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            if user is not None:
                obj = ResetPassword.objects.create(
                    token=ResetPassword.get_unique_token(),
                    user=user
                )
                # TODO: send email to user...
        except:
            pass
        return Response({"message": "Email sent"})


class ChangePassword(APIView):
    def post(self, request, token):
        obj = get_object_or_404(ResetPassword, token=token)
        new_pass = request.data.get("password")
        user = obj.user
        user.set_password(new_pass)
        user.save()
        return Response({"message": "Password Set"})
