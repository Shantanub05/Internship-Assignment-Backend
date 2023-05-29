# Import viewsets from Django REST framework, models, and serializers from the current app
from rest_framework import viewsets
from .models import Event, UserEvent
from .serializers import EventSerializer, UserEventSerializer

# EventViewSet handles CRUD operations for the Event model
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()  # Retrieve all Event instances from the database
    serializer_class = EventSerializer  # Use the EventSerializer to serialize Event instances

# UserEventViewSet handles CRUD operations for the UserEvent model
class UserEventViewSet(viewsets.ModelViewSet):
    queryset = UserEvent.objects.all()  # Retrieve all UserEvent instances from the database
    serializer_class = UserEventSerializer  # Use the UserEventSerializer to serialize UserEvent instances