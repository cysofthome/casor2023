from django.contrib import admin
from .models import *


admin.site.register(Leadership)
admin.site.register(RequestPayer)
admin.site.register(Testimony)
admin.site.register(Contact)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_host', 'event_date', 'event_location',)
    prepopulated_fields = {'slug': ('event_title',)}
    search_fields = ('event_title', 'event_date',  'event_location')

