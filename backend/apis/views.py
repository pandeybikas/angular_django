from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from db_connection.dal_access_layers import BaseAccessLayerClass
# Create your views here.

class ProjectMainViewSetClass(ViewSet):
    access_layer=BaseAccessLayerClass()

    @action(detail=False, methods=['get'], url_path='country_name')
    def get_country_name(self, request):
        data=self.access_layer.fetch_country_name()
        resp= data.to_dict(orient='records')
        return JsonResponse({'data': resp})


    @action(detail=False, methods=['get'], url_path='avg_depletion_rate')
    def get_avg_depletion_rate(self, request):
        country=self.request.GET.get('country', 'India')

        params = {
            'country': country
        }
        data= self.access_layer.fetch_avg_depletion_rate(**params)
        resp= data.to_dict(orient='records')
        return JsonResponse({'data': resp})
        
       
