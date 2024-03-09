from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff

