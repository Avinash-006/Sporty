
from django.urls import path, include
from . import views


urlpatterns= [
    path('live-updates/', include('liveupdatesapp.urls', namespace='liveupdatesapp')),
    path('', views.projectfrontpage, name='frontpage'),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.register, name='signup'),
    path('signup/signin/', views.UserLoginLogic, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('adminapp/', views.admin, name='admin'),
    path('signout/', views.logout, name='signout'),
path('calender/', views.calendar_page, name='calender'),
path('Dashboard/', views.dashboard, name='dashboard'),

]
