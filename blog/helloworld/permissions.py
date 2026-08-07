from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        current_user = request.user

        if obj.owner == current_user:
            return True

        return False
