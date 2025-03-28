from django.urls import path

from users.views import DeleteUserView, GetUsersView
from users.views.add_user import AddNewUserView

urlpatterns = [
    path("v1/events/<str:id>/participants/", GetUsersView.as_view(), name="get-user"),
    path("v1/events/<str:id>/participants/", AddNewUserView.as_view(), name="create-user"),
    path("v1/participants/<str:id>/", DeleteUserView.as_view(), name="delete-user")
]