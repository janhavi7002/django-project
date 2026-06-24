from django.urls import path
from home import views

urlpatterns = [

    path("", views.index, name="index"),

    path("login.html/", views.login_page, name="login_page"),
    path("signup.html/", views.signup_page, name="signup_page"),

    path("login/", views.login_user, name="login"),
    path("signup/", views.signup_view, name="signup"),

    path("verify-otp/", views.verify_otp, name="verify_otp"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("furm/", views.register, name="register"),

    path("profile/", views.profile, name="profile"),

    path("history/", views.history, name="history"),

    path("notifications/", views.notifications, name="notifications"),
]