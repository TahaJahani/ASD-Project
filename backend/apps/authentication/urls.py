from django.urls import path
from .views import *

app_name = "authentication"

urlpatterns = [
    path('test/', TestView.as_view()),
    path('login', LoginView.as_view()),
    path('sign-up', SignUpView.as_view()),
    path('logout', LogoutView.as_view())
]

