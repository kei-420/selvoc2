from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook, UsersManager
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import WordAddForm


class Home(LoginRequiredMixin, ListView):
    model = UserWordbook
    paginate_by = 10
    template_name = 'wordbook/home.html'

    def add_word(self, request, *args, **kwargs):
        user = UsersManager.objects.first()
        requesting_word = self.request.POST['word']
        existing_word = UserWordbook.objects.filter(user=user)
        if requesting_word in existing_word:
            adding_word = UserWordbook.objects.filter(word=requesting_word)
            context = {
                'adding_word': adding_word,
            }
            return render(request, 'wordbook/home.html', context)


class WordAddView(LoginRequiredMixin, CreateView):
    model = UserWordbook
    form_class = WordAddForm
    template_name = 'wordbook/create_word.html'
    success_url = reverse_lazy('wordbook:home')


