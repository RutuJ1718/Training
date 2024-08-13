from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('users/', views.user_list, name='user_list'),
    path('user/<str:email>/', views.user_detail, name='user_detail'),
]
