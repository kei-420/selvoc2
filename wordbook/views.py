from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook, Wordbook
from accounts.models import UsersManager
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import WordAddForm


class Home(LoginRequiredMixin, ListView):
    model = UserWordbook
    paginate_by = 10
    template_name = 'wordbook/home.html'


class WordAddView(LoginRequiredMixin, FormView):
    model = UserWordbook
    template_name = 'wordbook/create_word.html'
    form_class = WordAddForm()

    def get(self, request, *args, **kwargs):
        context = {
            'form': WordAddForm(),
        }
        return render(request, 'wordbook/create_word.html', context)

    def post(self, request, *args, **kwargs):
        form = WordAddForm(request.POST)
        if not form.is_valid():
            return render(request, 'wordbook/create_word.html', {'form': form})

        word_data = form.cleaned_data.get('word')
        exiting_word = Wordbook.objects.filter(vocabulary=word_data)
        # adding_word = Wordbook.objects.filter(userwordbook__word=exiting_word)
        context = {
            'vocabulary_list': exiting_word,
        }
        return render(request, 'wordbook/home.html', context)