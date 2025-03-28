
from events.views import CreateEventView
from django.urls import path
from events.views import FindEventByDateView

urlpatterns = [
     path('v1/create/event', CreateEventView.as_view(), name="create_event"),
     path('v1/find/event/date', FindEventByDateView.as_view(), name="find_event_by_date"),
]