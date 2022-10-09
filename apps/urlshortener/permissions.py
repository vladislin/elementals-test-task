from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create' and request.user.is_authenticated:
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy'] and request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user.owner or request.user.is_admin
        elif view.action in ['update', 'partial_update']:
            return obj == request.user.owner or request.user.is_admin
        elif view.action == 'destroy':
            return obj == request.user.owner or request.user.is_admin
        else:
            return False
