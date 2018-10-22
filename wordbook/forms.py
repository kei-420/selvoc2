from django import forms

from django.forms import ModelForm
from .models import UserWordbook


class WordAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(WordAddForm, self).__init__(*args, **kwargs)
        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserWordbook
        fields = ('word',)
        widgets = {
            'word': forms.TextInput(attrs={'placeholder': '単語'})
        }

    def clean_word(self):
        word = self.cleaned_data['word']
        if word not in UserWordbook.objects.get(word=word):
            raise forms.ValidationError(
                '%(error_word)sは認識されませんでした。',
                params={'error_word': word}
            )
        return word
