from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersManager(AbstractUser):
    """ユーザー管理モデル"""

    class Meta:
        db_table = 'user_manager'

    user_id = models.AutoField(
        verbose_name='ユーザーID',
        unique=True,
        primary_key=True,
    )
    username = models.CharField(
        verbose_name='ユーザー名',
        blank=False,
        unique=True,
        max_length=50,
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        blank=False,
        max_length=200,
    )
    is_active = models.BooleanField(
        verbose_name='アクティブ',
        default=True,
    )
    password = models.CharField(
        verbose_name='パスワード',
        blank=False,
        max_length=200,
    )
    date_joined = models.DateTimeField(
        verbose_name='登録日時',
        auto_now_add=True,
    )

    def __str__(self):
        return self.username
