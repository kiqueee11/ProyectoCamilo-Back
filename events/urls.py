
from events.views import CreateEventView
from django.urls import path
from events.views import FindEventByDateView
from events.views.event_view import EditEventView, FindEventByTitleView, FindEventByTypeView

urlpatterns = [
     path('v1/create/event', CreateEventView.as_view(), name="create_event"),
     path('v1/find/event/date', FindEventByDateView.as_view(), name="find_event_by_date"),
     path('v1/find/event/type', FindEventByTypeView.as_view(), name="find_event_by_type"),
     path('v1/find/event/title', FindEventByTitleView.as_view(), name="find_event_by_title"),
     path('v1/edit/event/<int:id>', EditEventView.as_view(), name="edit_event"),
]