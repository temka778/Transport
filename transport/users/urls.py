from django.urls import path
from . import views as custom_views


urlpatterns = [
    path("signup/", custom_views.SignUp.as_view(), name="signup"),
    path("signup_done/", custom_views.signup_done, name="signup_done"),
    path("login/", custom_views.CustomLoginView.as_view(), name="login"),
    path('update/', custom_views.ProfileUpdateView.as_view(), name='profile_update'),
    path("logout/", custom_views.CustomLogoutView.as_view(), name="logout"),
    path("password_change/done/", custom_views.password_change_done_view, name="password_change_done"),
    path("password_change/", custom_views.CustomPasswordChangeView.as_view(), name="password_change"),
    path("password_reset_done/", custom_views.password_reset_done, name="password_reset_done"),
    path("password_reset/", custom_views.CustomPasswordResetView.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>/", custom_views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", custom_views.password_reset_complete_view, name="password_reset_complete"),
    path("", custom_views.Profile.as_view(), name="profile")
]