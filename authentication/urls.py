# multi_role_auth/urls.py
from django.urls import path, include
from authentication.views import UserRegistrationView, UserLoginView, UserLogoutView
from student.views import StudentRegistrationView

urlpatterns = [
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/auth/login/', UserLoginView.as_view(), name='user-login'),
    path('api/auth/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('api/auth/register/student/', StudentRegistrationView.as_view(), name='student-registration'),
    # Add other URLs here
]