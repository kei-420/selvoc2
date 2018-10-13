from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook


class Home(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
       return render(request, 'wordbook/home.html')