from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response, Request, status
from movies.models import Movie
from movies.permissions import CustomPermission
from movies.serializers import MovieSerializer


class MovieView(APIView, PageNumberPagination):
    permission_classes = [CustomPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_pagination = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_pagination, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    permission_classes = [CustomPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
