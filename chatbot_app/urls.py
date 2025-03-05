from django.urls import path
from .views import chatbot_view

urlpatterns = [
    path('', chatbot_view, name='chatbot'),  # Keeps the root route
    path('chatbot/', chatbot_view, name='chatbot_api'),  # Adds the chatbot API route
]
