from django.urls import path

from attendances.views import GetAttendancesByEventIdView, CreateUpdateAttendanceView
from attendances.views.get_event_attenders import GetEventAttenders

urlpatterns = [
    path('events/<int:event_id>/attendances/', GetAttendancesByEventIdView.as_view() , name='get-attendances-by-event-id'),
    path('attendances/', CreateUpdateAttendanceView.as_view() , name='create-update-attendances'),
    path('events/<int:event_id>/attenders/', GetEventAttenders.as_view() , name='get-attenders-by-event-id'),
]