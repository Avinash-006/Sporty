from django.urls import path
from . import views
app_name = 'chatbotapp'
urlpatterns = [

    path('chatbot_index', views.chatbot_index, name='chatbot_index'),
]
