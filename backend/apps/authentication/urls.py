from django.urls import path
from .views import *

app_name = "authentication"

urlpatterns = [
    path('test2/', TestView.as_view()),
    path('login', LoginView.as_view()),
    path('sign-up', SignUpView.as_view()),
    path('logout', LogoutView.as_view()),
    path('get-me', GetMeView.as_view()),
    path('edit', EditProfileView.as_view())
]

