from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'meal_type']
    search_fields = ['dish', 'short_description', 'recipe']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
       
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        
        queryset = Recipe.objects.all()
        category = self.request.query_params.get('category', None)
        meal_type = self.request.query_params.get('meal_type', None)
        search_query = self.request.query_params.get('search', None)

        if category:
            queryset = queryset.filter(category=category)
        if meal_type:
            queryset = queryset.filter(meal_type=meal_type)
        if search_query:
            queryset = queryset.filter(dish__icontains=search_query) | \
                       queryset.filter(short_description__icontains=search_query)
        if not queryset.exists():
            return Response("No results found", status=status.HTTP_404_NOT_FOUND)
        return queryset