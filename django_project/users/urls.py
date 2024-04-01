# users/urls.py

from django.urls import path, re_path
from .views import home, register_user, user_login, update_user, fake_delete_user, logout, logoutfromgoogle, UserUpdateView

urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', user_login, name = 'login'),
    path('update/', update_user, name='update'),
    path('delete/', fake_delete_user, name='delete'),
    path('update_profile/', UserUpdateView.as_view(), name='update_profile')
]

