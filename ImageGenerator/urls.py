from django.urls import path
from . import views

urlpatterns = [
    path("", views.generate_image, name="generate_image"),
    path("chatbot/", views.chatbot, name="chatbot"),
]
