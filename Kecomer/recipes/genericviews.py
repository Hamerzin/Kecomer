from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import RecipesModel
from .serializer import RecipesSerializer
from collections import defaultdict
from drf_yasg.utils import swagger_auto_schema


class RecipesViewset(ModelViewSet):
    serializer_class = RecipesSerializer
    queryset = RecipesModel.objects.all()

    @swagger_auto_schema(operation_summary="List Product", operation_description="This endpoint list a users")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        filter_queryset = self.filter_jefatura(serializer)
        return Response(filter_queryset)

    def filter_jefatura(self, serializer):
        new_query = defaultdict(list)
        for row in serializer.data:
            category = row.get('category')
            new_query[category].append(row)
        return new_query