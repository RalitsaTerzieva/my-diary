from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("profile/", views.UserProfileDetailsView.as_view(), name="profile-details" ),
    path(
        "profile/update",
        views.UserProfileUpdateView.as_view(),
        name="profile-update"
    ),
]