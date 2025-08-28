from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import home_page_view, RegisterUserView

urlpatterns = [
    path('', home_page_view, name='home-page'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]