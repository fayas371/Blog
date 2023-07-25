from django.urls import path

from .views import *

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_proile',UserEditView.as_view(),name='edit-profile'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'),name='password-change'),
    path('password_success',password_success,name='password_success'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name="show_profile"),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name="edit_profile_page"),
    path('create_profile_page/',CreateProfilePageView.as_view(),name="create_profile_page"),
    path('login/',CustomLoginView.as_view(),name='login'),
]
