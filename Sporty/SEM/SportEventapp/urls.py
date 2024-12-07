from django.urls import path
from . import views
from .views import create_event
from .views import EventDeleteView
urlpatterns = [
    path('', views.event_list, name='Events'),
    path('create-event/', views.create_event, name='create_event'),
path('events/delete/<int:pk>/', EventDeleteView.as_view(), name='delete_event'),

]
