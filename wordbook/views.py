from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserWordbook, Wordbook
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import WordAddForm


class Home(LoginRequiredMixin, ListView):
    model = UserWordbook
    paginate_by = 10
    template_name = 'wordbook/home.html'

    # def get(self, request, *args, **kwargs):
    #     login_user = UserWordbook.objects.filter(user=request.user)

    # def add_word(self, request, *args, **kwargs):
    #     form = WordAddForm(request.POST)
    #     if not form.is_valid():
    #         return render(request, 'wordbook/create_word.html', {'form': form})
    #
    #     word = form.save(commit=False)
    #     UserWordbook.objects.select_related('word').get(word=word)
    #     word.save()
    #
    #     context = {
    #         'word': word,
    #     }
    #     return render(request, 'wordbook/home.html', context)


class WordAddView(LoginRequiredMixin, FormView):
    model = Wordbook
    template_name = 'wordbook/create_word.html'
    success_url = reverse_lazy('wordbook:home')
    form_class = WordAddForm()

    def form_valid(self, form):
        form = WordAddForm(self.request.POST)
        if not form.is_valid():
            return render(self.request, 'wordbook/create_word.html', {'form': form})
        # adding_word = get_object_or_404(Wordbook, pk=word_id)
        # adding_word = UserWordbook(word=, user=request.user).save()
        adding_word = self.request.choice.field
        context = {
            'vocabulary_list': adding_word,
        }
        return render(self.request, 'wordbook/home.html', context)


    # def get(self, request, *args, **kwargs):
    #     # vocabulary_set = Wordbook.objects.all()
    #     context = {
    #         'form': WordAddForm(),
    #         'num': enumerate(Wordbook.objects.all())
    #         #     'vocabulary_set': vocabulary_set,
    #         #     'num': enumerate(vocabulary_set),
    #     }
    #     return render(request, 'wordbook/create_word.html', context)

    # def post_word(self, request, word_id, *args, **kwargs):
    #     form = WordAddForm(request.POST)
    #     if not form.is_valid():
    #         return render(request, 'wordbook/create_word.html', {'form': form})
    #     adding_word = get_object_or_404(Wordbook, pk=word_id)
    #     # adding_word = UserWordbook(word=, user=request.user).save()
    #     context = {
    #         'vocabulary_list': adding_word,
    #     }
    #     return render(request, 'wordbook/home.html', context)
#
# class WordAddView(LoginRequiredMixin, View):
#     model = UserWordbook
#     template_name = 'wordbook/create_word.html'
#
#     def get(self, request, *args, **kwargs):
#         vocabulary_set = Wordbook.objects.all()
#
#         context = {
#             'vocabulary_set': vocabulary_set,
#             'num': vocabulary_set.count(),
#         }
#         return render(request, 'wordbook/create_word.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = WordAddForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'wordbook/create_word.html', {'form': form})
#
#         adding_word = form.vocabulary
#
#         context = {
#             'adding_word': adding_word,
#         }
#         return render(request, 'wordbook/home.html', context)

# def form_valid(self, form):
#     result = super(WordAddView, self).form_valid(form)
#     return result

# class WordAddView(LoginRequiredMixin, View):
#     model = Wordbook
#
#     def get(self, request, *args, **kwargs):
#         form = WordAddForm()
#         if not form.is_valid():
#             return render(request, 'wordbook/create_word.html', {'form': form})
#
#         form.fields['vocabulary'].queryset = Wordbook.objects.filter(vocabulary=)

#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': WordAddForm(),
#         }
#         return render(request, 'wordbook/create_word.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = WordAddForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'wordbook/create_word.html', {'form':form})
#
#         login_user = UserWordbook.objects.filter(user=request.user)
#         if login_user:
#             word = super(WordAddView, self).post(form)
#             return word
# #
# model = Memo
#     form_class = MemoForm
#     success_url = reverse_lazy('memo_list')
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         messages.success(
#             self.request, '「{}」を作成しました'.format(form.instance))
#         return result
