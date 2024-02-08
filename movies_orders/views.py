from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies_orders.serializers import MovieOrderSerializer
from rest_framework.permissions import IsAuthenticated


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int):
        find_movie = get_object_or_404(Movie.objects.all(), id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, movie=find_movie)

        return Response(serializer.data, status.HTTP_201_CREATED)
