from rest_framework.permissions import BasePermission


class MaintenancePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.group in ["maintenance", "manager"]
        return False


class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.group == "manager"
        return False
