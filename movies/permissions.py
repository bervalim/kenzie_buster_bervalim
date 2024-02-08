from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import Request, APIView


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_employee
        )


class MovieDetailPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
