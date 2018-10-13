from django.urls import path
from . import views


app_name = 'wordbook'
urlpatterns = [
    path('user_wordbook/', views.Home.as_view(), name='home'),
]
