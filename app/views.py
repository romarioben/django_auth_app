from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

# Create your views here.

class MyLoginView(LoginView):
    pass

class MyLogoutView(LogoutView):
    pass

class MyPasswordChangeView(PasswordChangeView):
    pass

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    pass


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    pass


class MyPasswordResetDoneView(PasswordResetDoneView):
    pass



class MyPasswordResetView(PasswordResetView):
    pass



class My