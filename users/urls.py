from django.urls import path
from users.views.add_user import AddNewUserView

urlpatterns = [
    path("v1/events/<str:id>/participants", AddNewUserView.as_view(), name="create-user")
]