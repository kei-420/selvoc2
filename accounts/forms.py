from django import forms

from .models import UsersManager
from django.forms import ModelForm
from wordbook.models import UserWordbook


class SignUpForm(ModelForm):
    class Meta:
        model = UsersManager
        fields = ('username', 'email', 'password',)
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'パスワード'}),
        }

    confirm_password = forms.CharField(
        label='確認用パスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '確認用パスワード'}),
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'ユーザー名'}
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("パスワードと確認用パスワードが一致しません。")

    def create_wordbook(self, created, instance):
        if created:
            UserWordbook.objects.create(user=instance)
            UsersManager.objects.create(user=instance.id)




