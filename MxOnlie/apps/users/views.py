# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .models import UserProfile
from forms import LoginForm


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', "")
            pass_word = request.POST.get('password', "")
            print 'user_name = ', user_name, '\n', 'pass_word = ', pass_word
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': u'用户名或密码错误!'})

# def user_login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username', "")
#         pass_word = request.POST.get('password', "")
#         print 'user_name = ', user_name, '\n', 'pass_word = ', pass_word
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': u'用户名或密码错误!'})
#         pass
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})
