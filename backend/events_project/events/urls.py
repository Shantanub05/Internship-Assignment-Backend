# Import path and include functions from Django, and DefaultRouter from Django REST framework
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Import the views from the current app
from . import views

# Create a default router for the API
router = DefaultRouter()
# Register the EventViewSet with the router using the 'events' prefix
router.register(r'events', views.EventViewSet)
# Register the UserEventViewSet with the router using the 'user-events' prefix
router.register(r'user-events', views.UserEventViewSet)

# Define the urlpatterns list which includes the router's URLs
urlpatterns = [
    path('', include(router.urls)),
]