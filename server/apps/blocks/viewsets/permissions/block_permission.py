from django.conf import settings

from rest_framework import permissions


class BlockPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if settings.DEBUG and request.method in ['POST', 'PATCH']:
                return True
        return True
