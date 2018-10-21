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
