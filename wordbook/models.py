from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import UsersManager


class Wordbook(models.Model):
    """参照元単語リストモデル"""
    class Meta:
        db_table = 'wordbook'

    word = models.AutoField(
        verbose_name='単語ID',
        unique=True,
        primary_key=True,
    )
    vocabulary = models.CharField(
        verbose_name='単語',
        max_length=150,
    )
    word_class = models.CharField(
        verbose_name='品詞',
        max_length=20,
        blank=True,
    )
    word_meaning = models.TextField(
        verbose_name='意味',
        blank=False,
    )
    created_datetime = models.DateTimeField(
        verbose_name='作成日時',
        auto_now_add=True,
    )
    updated_datetime = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True,
    )

    def __str__(self):
        return str(self.word) + ', ' + self.vocabulary


class UserWordbook(models.Model):
    """ユーザー単語帳モデル"""

    class Meta:
        db_table = 'user_wordbook'

    user_wordbook = models.AutoField(
        verbose_name='ユーザー単語帳ID',
        unique=True,
        primary_key=True,
    )
    word = models.ForeignKey(
        Wordbook,
        verbose_name='単語ID',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        UsersManager,
        verbose_name='ユーザーID',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return str(self.user_wordbook) + ', ' + str(self.word) + ', ' + str(self.user)


