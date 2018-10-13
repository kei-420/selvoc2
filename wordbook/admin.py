from django.contrib import admin
from .models import Wordbook, UserWordbook


admin.site.register(Wordbook)
admin.site.register(UserWordbook)
