from django.shortcuts import render,redirect
from django import forms
from django.forms.forms import Form
from . import models, forms
from django.views.generic import CreateView, FormView, RedirectView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib.auth.views import LoginView as LogView



class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = forms.UserSignupForm
    success_url = reverse_lazy("users:login")

class LoginView(LogView):
    template_name = "users/login.html"
    sucess_url = reverse_lazy("listapp:indexpage")
    form_class = forms.UserLoginForm
    redirect_authenticated_user= True

    # def get(self,request):
    #     return render(request, self.template_name, {"form":forms.UserLoginForm()})
    # def post(self,request):
    #     form = forms.UserLoginForm(request, request.POST)
    #     if form.is_valid():
    #         user = authenticate(request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
        
    #         if not user:
    #             return render(request, self.template_name, {"form":forms.UserLoginForm(), "invalid_creds":True})
    #         login(request, user)
       
    #     return redirect(reverse("listapp:indexpage"))

class LogoutView(RedirectView):
    url = reverse_lazy("users:login")

    def get(self, request, *args, **kwrgs):
        logout(request)
        return super(LogoutView,self).get(request, *args, **kwrgs)








