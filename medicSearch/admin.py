from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_at'
  list_display = ('user', 'role', 'birthday')
  list_display_links = ('user', 'role')
  list_filter = ('user__is_active',)
  fields = ('user',('role'), 'image', 'birthday', 'specialties', 'addresses')
  empty_value_display = '--empty--'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Addresses)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
