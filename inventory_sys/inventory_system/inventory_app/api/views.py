from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED
)
from rest_framework.exceptions import ValidationError
from rest_framework import generics, mixins

from inventory_app.models import CarInventory
from inventory_app.api.serializers import CarInventorySerializer


class CarInventoryList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = CarInventory.objects.all()
    serializer_class = CarInventorySerializer

    def get(self, request, *args, **kwargs):

        try:
            return Response({
                'data':self.list(request,*args,**kwargs).data,
                'status':'Fetch Sucessful'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Fetch Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request,*args,**kwargs):

        try:
            if len(request.data) == 0:
                return Response({
                    'status':'Failed',
                    'errors':'Recieved Empty Object'
                },status=HTTP_400_BAD_REQUEST)
            
            serialzer = self.get_serializer(data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Sucess'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)

            
        except ValidationError as ve:
            return Response({
                'status':'Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)

class CarInventoryDetails(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = CarInventory.objects.all()
    serializer_class = CarInventorySerializer

    def get(self,request,*args,**kwargs):

        try:
            return Response({
                'data':self.retrieve(request,*args,**kwargs).data,
                'status':'Success'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, *args, **kwargs):

        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'status':'Deletion Sucessful',

            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Deletion Failed',
                'errors':str(e)
            })
    

