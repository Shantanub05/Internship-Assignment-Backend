# Import the built-in User model from Django and the models module
from django.contrib.auth.models import User
from django.db import models

# Event model representing an individual event
class Event(models.Model):
    event_name = models.CharField(max_length=255)  # Name of the event
    date = models.DateField()  # Date of the event
    time = models.TimeField()  # Time of the event
    location = models.CharField(max_length=255)  # Location of the event
    image = models.ImageField(upload_to='event_images/')  # Image related to the event
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the event

    # String representation of the event
    def __str__(self):
        return self.event_name

# UserEvent model representing the relationship between a user and an event
class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User associated with the event
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Event associated with the user
    is_liked = models.BooleanField(default=False)  # Boolean indicating if the user likes the event

    # String representation of the UserEvent
    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"