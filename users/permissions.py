from django.views import View
from rest_framework import permissions
from rest_framework.request import Request
from users.models import User


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: User
    ) -> bool:
        if (
            request.method == permissions.SAFE_METHODS
            and request.user.is_authenticated
        ):
            return True
        return request.user.id == obj.id or request.user.is_superuser
