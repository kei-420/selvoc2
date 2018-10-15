from django import forms

from .models import UsersManager
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django.core.exceptions import ObjectDoesNotExist
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

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力して下さい',
                params={'min_length': 3}
            )
        return username

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("パスワードと確認用パスワードが一致しません。")


class LoginForm(forms.Form):
    username = UsernameField(
        label='ユーザー名',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'ユーザー名',
                                      'autofocus': True})
        )

    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'パスワード'}, render_value=True)
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean_password(self):
        data = self.cleaned_data['password']
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) < 3:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力して下さい',
                params={'min_length': 3}
            )
        return data

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = UsersManager.objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError('正しいユーザー名を入力して下さい。')
        if not user.check_password(password):
            raise forms.ValidationError('正しいユーザー名とパスワードを入力して下さい。')

        self.user_cache = user

    def get_user(self):
        return self.user_cache

