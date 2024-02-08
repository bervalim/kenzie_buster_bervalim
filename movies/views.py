from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer
from .models import Movie
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request):
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, request)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int):
        find_movie = get_object_or_404(Movie.objects.all(), id=movie_id)

        self.check_object_permissions(request, find_movie)

        serializer = MovieSerializer(find_movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int):
        find_movie = get_object_or_404(Movie.objects.all(), id=movie_id)

        self.check_object_permissions(request, find_movie)

        find_movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
