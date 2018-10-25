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

    # def get_queryset(self):
    #     self.request.user = get_object_or_404(UsersManager, name=self.kwargs['username'])
    #     return UsersManager.objects.filter(username=self.request.user)


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
        # login_user = UserWordbook.objects.get(user=request.POST.user)
        # word_data = form.cleaned_data.get('word')
        # word_data = form.save(commit=False)
        # queryset = Wordbook.objects.all()
        # inner_join = Wordbook.objects.select_related('word')
        #
        # context = {
        #         'word_data': word_data,
        #         'vocabulary_list': inner_join,
        #         'queryset': queryset,
        # }
        #
        # word_data.save()
        # return render(request, 'wordbook/home.html', context)
            # get_user = UserWordbook.objects.get(user=login_user)
        # login_user = UsersManager.objects.first()
        word_data = form.cleaned_data.get('word')
        exiting_word = Wordbook.objects.filter(vocabulary=word_data)
        # adding_word.word =
        # adding_word = UsersManager.objects.filter().add(word_data)

        # inner_join = Wordbook.objects.filter(userwordbook__user_id=login_user.user_id)
        # inner_join.word = word_data
        context = {
            'word_data': word_data,
            'vocabulary_list': exiting_word,
        }
        return render(request, 'wordbook/home.html', context)