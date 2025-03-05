from django.urls import path
from .views import convert_text

urlpatterns = [
    path('', convert_text, name='convert_text'),
]
