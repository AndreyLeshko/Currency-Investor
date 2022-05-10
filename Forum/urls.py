from django.urls import path
from Forum.views import main_page, log_in
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_page),
    # path('log-in/', log_in, name='log-in'),
    path('log-in', auth_views.LoginView.as_view(), name='login'),
    path('log-out', auth_views.LogoutView.as_view(), name='logout'),
    ]