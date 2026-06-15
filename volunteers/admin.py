from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display  = ('name', 'skill', 'city', 'email', 'phone', 'joined_date', 'is_active')
    search_fields = ('name', 'email', 'city', 'skill')
    list_filter   = ('skill', 'city', 'is_active')