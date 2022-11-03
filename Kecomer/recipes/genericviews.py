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
        queryset =self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)