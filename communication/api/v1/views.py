from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from communication.models import Waitlist, ContactForm
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from abegify.pagination import CustomPagination
from .serializers import WaitlistSerializer, ContactFormSerializer




class WaitlistViewSet(viewsets.ViewSet):
    """
    Viewset for creating and viewing waitlist.
    """
    serializer_class = WaitlistSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def list(self, request):
        queryset = Waitlist.objects.all().order_by('-id')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class ContactFormViewSet(viewsets.ViewSet):
    """
    Viewset for sending contact form.
    """
    serializer_class = ContactFormSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def list(self, request):
        queryset = ContactForm.objects.all().order_by('-id')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
