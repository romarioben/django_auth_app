from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.contrib.auth.decorators import login_required
from . import forms
from django.views import View

# Create your views here.

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'auth_app/login.html'
    pass

class MyLogoutView(LogoutView):
    pass

class MyPasswordChangeView(PasswordChangeView):
       pass

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth_app/password_change_complete.html'
    pass


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = forms.MySetPasswordForm
    template_name = 'auth_app/password_change.html'
    pass


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth_app/password_reset_done.html'
    pass

class MyPasswordResetView(PasswordResetView):
    form_class = forms.PasswordResetForm
    template_name = 'auth_app/password_reset.html'
    pass

class MyRegistrationView(View):
    def get(self, request):
        form = forms.SignupForm()
        print(form)
        return render(request, "auth_app/registration.html", locals())
    
    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "auth_app/registration.html", locals())
        
        

@login_required
def home(request):
    return render(request, "auth_app/home.html", locals())

@login_required
def verify_email(request):
    return render(request, "auth_app/verify_email.com", locals())