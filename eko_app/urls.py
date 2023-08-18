from django.urls import path
from .views import add_solution

urlpatterns = [
    # запросы на страницы сайта
    path('addsolution/', add_solution),
]