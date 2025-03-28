
from events.views import CreateEventView
from django.urls import path

urlpatterns = [
     path('v1/create/event', CreateEventView.as_view(), name="create_event"),
]