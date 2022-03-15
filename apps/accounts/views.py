from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .api.serializers import CreateUserSerializer, DetailUserSerializer
from .api.services.create_user_service import CreateUserService

class CreateUserView(APIView):

    @swagger_auto_schema(request_body=CreateUserSerializer, responses={200: openapi.Response('CREATED', DetailUserSerializer), 500: openapi.Response('INTERNAL SERVER ERRO')})
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            create_user_service = CreateUserService(serializer.data)
            user = create_user_service.execute()
            detail_user_serializer = DetailUserSerializer(user)
            return Response(detail_user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

create_user_view = CreateUserView.as_view()
