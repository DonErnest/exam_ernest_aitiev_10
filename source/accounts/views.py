from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class SignUpUserView(CreateView):
    form_class = SignUpForm
    template_name = 'user/user_sign_up.html'
    success_url = reverse_lazy('accounts:login')


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    next_page = 'webapp:index'