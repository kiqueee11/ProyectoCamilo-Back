from django.urls import path

from attendances.views import GetAttendancesByEventIdView, CreateUpdateAttendanceView, GetEventAttendanceStadisticsView
from attendances.views.get_event_attenders import GetEventAttenders

urlpatterns = [
    #Devuelve toda la asistencia general del evento, devuelve todos los usuarios ligados al evento
    # (da igual si attendance = true o false)
    path('events/<int:event_id>/attendances', GetAttendancesByEventIdView.as_view() , name='get-attendances-by-event-id'),

    #Crear y actualizar una attendance
    #Si le envías en la request el ID de attendance, actualiza el objeto con dicho ID. Solo hace falta enviar
    # --> (attendance)

    #Si quieres crear una nueva, se omite el ID. Solo hace falta enviar
    # --> (attendance, user (ID), event (ID))
    path('attendances', CreateUpdateAttendanceView.as_view() , name='create-update-attendances'),

    #Devuelve todos los ASISTENTES del evento (attendance = true)
    path('events/<int:event_id>/attenders', GetEventAttenders.as_view() , name='get-attenders-by-event-id'),

    #Devuelve pequeña estadística general del evento (número de personas registradas, asistentes y las personas que no asistieron)
    path('events/<int:event_id>/stadistics', GetEventAttendanceStadisticsView.as_view() , name='get-event-stadistics-by-event-id'),
]