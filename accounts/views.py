from django.conf import settings

from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from wordbook.models import UserWordbook
from .models import UsersManager


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': SignUpForm(),
        }
        return render(request, 'accounts/signup.html', context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/signup.html', {'form': form})

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        self.create_wordbook()
        auth_login(request, user)
        return redirect('accounts:login')

    @staticmethod
    def create_wordbook(request, instance, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            UserWordbook.objects.all().select_related('user_id')
            UsersManager.objects.get(user_id=instance)
            UserWordbook.objects.create(user_id=instance.id)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')
