from django.contrib import admin
from .models import Event, UserEvent


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'time', 'location', 'user')
    search_fields = ('event_name', 'location', 'user__username')


class UserEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'is_liked')
    list_filter = ('is_liked',)
    search_fields = ('user__username', 'event__event_name')


admin.site.register(Event, EventAdmin)
admin.site.register(UserEvent, UserEventAdmin)