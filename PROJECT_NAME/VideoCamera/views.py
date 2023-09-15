from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django_celery_results.models import TaskResult

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions



# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class APIPermissions(DjangoModelPermissions):
    """ requires authentication for all get, post, put, patch, and delete methods"""
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class BaseAPIView(viewsets.ModelViewSet):
    """ Base class for all API views / endpoints """
    filterset_fields = '__all__'
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [APIPermissions]
    filter_backends = [DjangoFilterBackend]
    paginator_class = StandardResultsSetPagination



