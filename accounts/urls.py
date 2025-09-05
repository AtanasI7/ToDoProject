from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import home_page_view, RegisterUserView, UserDetailsView, UserEditView, UserDeleteView

urlpatterns = [
    path('', home_page_view, name='home-page'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='profile-details'),
        path('edit/', UserEditView.as_view(), name='profile-edit'),
        path('delete/', UserDeleteView.as_view(), name='profile-delete'),
    ])),

]