from rest_framework.response import Response

from users.serializers import UsersSerializers
from users.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from drf_yasg.utils import swagger_auto_schema


class ClientViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializers

    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_summary="List user", operation_description="This endpoint list a users")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





    