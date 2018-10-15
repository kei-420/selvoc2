import logging

from django.conf import settings
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from .forms import SignUpForm, LoginForm
from wordbook.models import UserWordbook, Wordbook
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
        # get_user_id = user.user_id
        # UserWordbook.objects.get_or_create(
        #     pk=get_user_id
        # )
        user.set_password(form.cleaned_data['password'])
        user.save()
        get_user_id = UsersManager.objects.get(pk=user.user_id)
        UserWordbook.objects.get_or_create(user=get_user_id)
        # get_word = Wordbook.objects.get(word_id=user.word_id)
        # for word in get_word:
        #     Wordbook.objects.filter(pk=word)
        #     UserWordbook.objects.get_or_create(word=word)

        auth_login(request, user)
        return redirect('accounts:login')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('wordbook:home'))

        context = {
            'form': LoginForm(),
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})

        user = form.get_user()
        auth_login(request, user)

        return redirect(reverse('wordbook:home'))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect(reverse('accounts:login'))



