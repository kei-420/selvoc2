from django.contrib import messages

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook, Wordbook
from accounts.models import UsersManager
from django.db.models import Q
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import WordAddForm


# class Home(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         queryset = UserWordbook.objects.select_related('word').order_by('word__vocabulary')
#         key_word = request.GET.get('key_word')
#         if key_word:
#             queryset = queryset.filter(
#                 Q(word__vocabulary__exact=key_word)
#             )
#         context = {
#             'key_word': key_word,
#             'word_list': queryset,
#         }
#         return render(request, 'wordbook/home.html', context)
class Home(LoginRequiredMixin, ListView):
    template_name = 'wordbook/home.html'
    model = UserWordbook


class WordAddView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': WordAddForm(),
        }
        return render(request, 'wordbook/create_word.html', context)

    def post(self, request, *args, **kwargs):
        form = WordAddForm(request.POST)
        if not form.is_valid():
            return render(request, 'wordbook/create_word.html', {'form': form})

        word_data = form.cleaned_data.get('adding_word')
        word_list = Wordbook.objects.select_related().all()
        adding_word = word_list.filter(vocabulary=word_data).values()

        if adding_word:
            context = {
                'vocabulary_list': adding_word,
            }
            return render(request, 'wordbook/home.html', context)
