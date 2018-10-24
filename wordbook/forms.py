from django import forms

from django.forms import ModelForm
from .models import Wordbook


class WordAddForm(forms.Form):
    vocabulary_list = forms.ModelChoiceField(
        queryset=Wordbook.objects.all(),
        label='追加単語',
        to_field_name='vocabulary'
    )

    # class Meta:
    #     model = Wordbook
    #     fields = ['vocabulary_list', ]
    # def __init__(self, queryset, *args, **kwargs):
    #     super(WordAddForm, self).__init__(*args, **kwargs)
    #     self.fields['vocabulary_list'] = queryset
    #     if queryset:
    #         self.fields['vocabulary_list'] = queryset
    # def __init__(self, queryset=None, *args, **kwargs):
    #     super(WordAddForm, self).__init__(*args, **kwargs)
    #     self.fields['vocabulary_list'] = queryset
    #     if queryset:
    #         self.fields['vocabulary_list'].queryset = queryset

    # def __int__(self, *args, **kwargs):
    #     super(WordAddForm, self).__int__(*args, **kwargs)
    #     self.fields['vocabulary'].widget.attrs = {'placeholder': '追加単語'}
    #
    # def clean_vocabulary(self):
    #     vocabulary = self.cleaned_data['vocabulary']
    #     vocabulary_set = Wordbook.objects.filter(vocabulary=vocabulary)
    #     if vocabulary_set:
    #         return vocabulary
    #     else:
    #         forms.ValidationError(
    #             '%(error_vocab)sは存在しません。',
    #             params={'error_vocab': vocabulary}
    #         )

    # def __init__(self, queryset=None, *args, **kwargs):
    #     super(WordAddForm, self).__init__(*args, **kwargs)
    #     self.fields['vocabulary'] = queryset
    #     if queryset:
    #         self.fields['vocabulary'].queryset = queryset
    #
    # def clean_vocabulary(self):
    #     vocabulary = self.cleaned_data['vocabulary']
    #     vocabulary_set = Wordbook.objects.all()
    #     for v in vocabulary_set:
    #         if vocabulary == Wordbook.objects.filter(vocabulary=v):
    #             return vocabulary
    #         else:
    #             forms.ValidationError(
    #                 '%(error_vocab)sは存在しません。',
    #                 params={'error_vocab': 3},
    #             )


