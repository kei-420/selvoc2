import logging

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import UsersManager

logger = logging.getLogger(__name__)


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
        unique=True,
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
        return self.vocabulary


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
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        UsersManager,
        verbose_name='ユーザーID',
        related_name='login_user',
        on_delete=models.PROTECT,
    )

    is_understood = models.BooleanField(
        verbose_name='ユーザー理解度',
        blank=False,
        null=False,
        default=False,
    )

    # def __init__(self, word, user, *args, **kwargs):
    #    super(UserWordbook, self).__init__(self, *args, **kwargs)
    #    self.word = word
    #    self.user = user
    #    logger.info("__init__.UserWordbookの中にいます。")

    def __str__(self):
        return str(self.word)
