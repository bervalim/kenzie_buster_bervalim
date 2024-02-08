from rest_framework.permissions import BasePermission
from rest_framework.views import Request
from users.models import User


class UsersDetailsPermission(BasePermission):
    def has_object_permission(self, request: Request, view, obj: User):
        return request.user.is_employee or obj == request.user
