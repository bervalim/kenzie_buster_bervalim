from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.permissions import UsersDetailsPermission
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UsersDetailsPermission]

    def get(self, request: Request, user_id: int):
        find_user = get_object_or_404(User.objects.all(), id=user_id)

        self.check_object_permissions(request, find_user)

        serializer = UserSerializer(find_user)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int):
        find_user = get_object_or_404(User.objects.all(), id=user_id)

        self.check_object_permissions(request, find_user)

        serializer = UserSerializer(find_user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
