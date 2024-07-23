from django.contrib import admin
from .models import Building, Room, Resident, MaintenanceRequest

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'building_name', 'address', 'total_floors')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_number', 'floor', 'vacancy', 'status', 'building')
    list_filter = ('status', 'floor', 'building')


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('resident_id', 'university_id',  'name', 'email', 'phone_number', 'resident_type', 'admission_date', 'checkout_date', 'room')
    list_filter = ('admission_date', 'checkout_date', 'resident_type', 'room')

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'room', 'request_date', 'description', 'status')
    list_filter = ('status', 'room')
