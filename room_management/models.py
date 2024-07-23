from django.db import models

class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_floors = models.IntegerField()

    def __str__(self):
        return self.building_name



class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    vacancy = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Under Maintenance', 'Under Maintenance')])
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room {self.room_number} - {self.building.building_name}"


class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True)
    university_id = models.IntegerField() 
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    resident_type = models.CharField(max_length=15,choices=[
        ('student', 'Student'), ('staff','Staff'), ('guest','Guest')
    ])
    admission_date = models.DateField()
    checkout_date = models.DateField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class MaintenanceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    request_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Maintenance Request {self.request_id} - Room {self.room.room_number}"
