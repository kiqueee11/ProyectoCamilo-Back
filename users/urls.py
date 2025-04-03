from django.urls import path

from users.views import DeleteUserView, GetUsersView, AddUserToEventView
from users.views.check_user import checkUserView
from users.views.create_user import CreateNewUserView

urlpatterns = [
    path("v1/events/<slug:slug>/participants/", GetUsersView.as_view(), name="get-user"),
    path("v1/create-user/", CreateNewUserView.as_view(), name="create-user"),
    path("v1/participants/<slug:slug>/", DeleteUserView.as_view(), name="delete-user"),
    path("v1/events/<slug:slug>/participants/add", AddUserToEventView.as_view(), name="add-user-to-event"),
    path("v1/check/user/", checkUserView.as_view(), name="get-user"),

]