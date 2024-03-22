# users/urls.py

from django.urls import path
from .views import register_user, user_login, update_user, fake_delete_user, logout


urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', user_login, name = 'login'),
    path('update/', update_user, name='update'),
    path('delete/', fake_delete_user, name='delete'),
    path('logout/', logout, name='logout')
]

