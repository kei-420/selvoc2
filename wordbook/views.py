from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, \
    HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import WordAddForm


class Home(LoginRequiredMixin, View):
    model = UserWordbook
    paginate_by = 10
    template_name = 'wordbook/home.html'

    def get(self, request, *args, **kwargs):
        queryset = UserWordbook.objects.prefetch_related('word')
        shown_word = request.GET.get('shown_word')
        if shown_word:
            context = {
                'shown_word': shown_word,
                'word_list': queryset,
            }
            return redirect(request, 'wordbook:home', context)

    def post(self, request, *args, **kwargs):
        form = WordAddForm
        if not form.is_valid():
            return render(request, 'wordbook/home.html', {'form': form})

        adding_word = form.save(commit=True)
        adding_word.save()
        get_word_id = UserWordbook.objects.get(pk=adding_word.word)
        UserWordbook.objects.get_or_create(adding_word=get_word_id)
        return HttpResponseRedirect(reverse_lazy('wordbook:home'))


class WordAddView(LoginRequiredMixin, CreateView):
    model = UserWordbook
    form_class = WordAddForm
    template_name = 'wordbook/create_word.html'
    success_url = reverse_lazy('wordbook:home')

    # model = UserWordbook
    # context_object_name = 'word'
    # template_name = 'wordbook/home.html'
    #
    # def get_context_data(self, **kwargs):
    #     kwargs['word'] = self.word
    #     return super().get_context_data(**kwargs)
    #
    # def get_queryset(self):
    #     self.word = get_object_or_404(UserWordbook, pk=self.kwargs.get('pk'))
    #     queryset = self.word.word.order_by()