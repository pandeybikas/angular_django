from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

# Create your views here.

class ProjectMainViewSetClass(ViewSet):
    @action(detail=False, methods=['get'], url_path='my_test_api')
    def get_my_test_api(self, request):
        return JsonResponse({'data': 'test api success'})
