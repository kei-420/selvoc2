from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook


class Home(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        wordbook = get_object_or_404(UserWordbook, pk=user_id)
        context = {
            'wordbook': wordbook
        }
        return render(request, 'wordbook/home.html', context)
