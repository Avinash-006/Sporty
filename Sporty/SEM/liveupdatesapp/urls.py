from django.urls import path
from . import views
app_name = 'liveupdatesapp'
urlpatterns = [
    path('live-updates/', views.live_updates, name='live_updates'),
    # other url patterns
]
