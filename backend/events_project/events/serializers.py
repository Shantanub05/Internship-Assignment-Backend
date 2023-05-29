# Import serializers from Django REST framework and the models from the current app
from rest_framework import serializers
from .models import Event, UserEvent

# EventSerializer is a serializer for the Event model
class EventSerializer(serializers.ModelSerializer):
    # Meta class contains the configuration for the serializer
    class Meta:
        model = Event  # Specify the model to use
        # Define the fields that should be serialized
        fields = ['event_name', 'date', 'time', 'location', 'image', 'user']

# UserEventSerializer is a serializer for the UserEvent model
class UserEventSerializer(serializers.ModelSerializer):
    # Meta class contains the configuration for the serializer
    class Meta:
        model = UserEvent  # Specify the model to use
        # Define the fields that should be serialized
        fields = ['user', 'event', 'is_liked']