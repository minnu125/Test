from django.urls import path
from demoapp.views import Rational

urlpatterns = [
    path('arithmetic/', Rational.as_view()),
]