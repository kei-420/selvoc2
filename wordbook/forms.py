from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from .models import Wordbook, UserWordbook


# class WordAddForm(forms.Form):
#     word = forms.ModelChoiceField(
#         queryset=Wordbook.objects.all(),
#         label='追加単語',
#         to_field_name='vocabulary',
#     )
#
#     def __int__(self, *args, **kwargs):
#         super(WordAddForm, self).__int__(*args)
#
#     def clean_word(self):
#         word = self.cleaned_data['word']
#         return word

class WordAddForm(forms.Form):
    adding_word = forms.CharField(
        label='追加単語',
        max_length=255,
    )

    def __init__(self, *args, **kwargs):
        super(WordAddForm, self).__init__(*args, **kwargs)
        self.word_cache = None

    def clean_adding_word(self):
        adding_word = self.cleaned_data['adding_word']
        try:
            word = Wordbook.objects.get(vocabulary=adding_word)
        except ObjectDoesNotExist:
            raise forms.ValidationError("正しい単語を入力してください。")
        self.word_cache = word
        return adding_word

    def get_word(self):
        return self.word_cache


# class WordAddForm(ModelForm):
#     listing_word = forms.ModelChoiceField(
#         label='追加単語',
#         queryset=Wordbook.objects,
#     )
#
#     class Meta:
#         model = UserWordbook
#         fields = ('word', )



