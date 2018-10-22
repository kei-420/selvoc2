import logging
import time

from django.conf import settings
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from .forms import SignUpForm, LoginForm
from wordbook.models import UserWordbook, Wordbook
from .models import UsersManager


logger = logging.getLogger(__name__)


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': SignUpForm(),
        }
        logger.info("You are in get.SignUpView")
        return render(request, 'accounts/signup.html', context)

    def post(self, request, *args, **kwargs):
        start_time = time.time()
        logger.info("You are in post.SignUpView")
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/signup.html', {'form': form})

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        for word in Wordbook.objects.all():
            uwb = UserWordbook()
            uwb.word = word
            uwb.user = user
            uwb.save()

        auth_login(request, user)

        logger.debug("Finished in {:.2f} sec.".format(time.time() - start_time))
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


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect(reverse('accounts:login'))



