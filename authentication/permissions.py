# authentication/permissions.py
from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'staff'

class IsMaintenance(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'maintenance'
    
class IsSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'security'
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'administrator'