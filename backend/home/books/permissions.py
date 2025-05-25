from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Check is owner.if owner, it will allow permission...
    """

    message = "Permission Denied.You are not owner."

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
