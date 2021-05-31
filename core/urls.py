from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user-register/', UserRegistrationView.as_view(), name='user-register'),
    # path('user-login/', views.LoginView.as_view(), name='user-login'),
    # path('user-logout/', views.UserLogout, name='user-logout'),
]
