from rest_framework import serializers
from datetime import datetime
from inventory_app.models import CarInventory



class CarInventorySerializer(serializers.ModelSerializer):
   

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = CarInventory
        exclude = ['created','updated']
    
    def get_created_at(self,object):
        return object.created.strftime('%Y-%m-%d-%H:%M:%S')
    
    def get_updated_at(self,object):
        return object.updated.strftime('%Y-%m-%d-%H:%M:%S')
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.model = validated_data.get('model',instance.model)
        instance.company_name = validated_data.get('company_name',instance.company_name)
        instance.description = validated_data.get('description',instance.description)
        instance.img = validated_data.get('img',instance.img)
        instance.price = validated_data.get('price',instance.price)
        instance.is_avaliable  = validated_data.get('is_avaliable ',instance.is_avaliable)

        instance.updated = datetime.now()
        instance.save()
        return instance 
