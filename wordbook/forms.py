from django import forms

from django.forms import ModelForm
from .models import Wordbook, UserWordbook


class WordAddForm(forms.Form):
    word = forms.ModelChoiceField(
        queryset=Wordbook.objects.all(),
        label='追加単語',
        to_field_name='vocabulary',
    )

    def __int__(self, *args, **kwargs):
        super(WordAddForm, self).__int__(*args)

    def clean_word(self):
        word = self.cleaned_data['word']
        return word




