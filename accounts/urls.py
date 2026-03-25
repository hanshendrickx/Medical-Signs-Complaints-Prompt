from django.urls import path
from .views import (
    home,
    about,
    CreateUserView,
    GuestUserView,
    LoginView,
    LogoutView,
    CurrentUserView,
    DeleteUserView,
    FamilyMembersView,
    DependentCreateView,
    DependentUpdateDeleteView,
    ProxyStatusView,
)


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("guest/", GuestUserView.as_view(), name="guest_signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", CurrentUserView.as_view(), name="me"),
    path("delete/", DeleteUserView.as_view(), name="delete"),
    path("family/", FamilyMembersView.as_view(), name="family"),
    path(
        "family/dependents/create/",
        DependentCreateView.as_view(),
        name="create_dependent",
    ),
    path(
        "family/dependents/<int:pk>/",
        DependentUpdateDeleteView.as_view(),
        name="dependent_detail",
    ),
    path("proxy-status/", ProxyStatusView.as_view(), name="proxy_status"),
]
