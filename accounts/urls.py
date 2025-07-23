from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import signup_view, login_view, logout_view , home_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
]
