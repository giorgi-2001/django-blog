from django.urls import reverse_lazy
from django.contrib.auth import views as pwd_views
from django.urls import path
from . import views


app_name = "users"


urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),

    path(
        "password/request-reset",
        pwd_views.PasswordResetView.as_view(
            template_name="users/password_reset.html",
            email_template_name="users/email.html",
            success_url=reverse_lazy("users:password_reset_done")
        ),
        name="password_reset"
    ),

    path(
        "password/request-reset-sent",
        pwd_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    path(
        "password/reset/<uidb64>/<token>/",
        pwd_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete")
        ),
        name="password_reset_confirm"
    ),

    path(
        "password/reset-done",
        pwd_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
        ),
        name="password_reset_complete"
    ),

]
