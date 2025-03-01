from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Job , category , apply


class jobserializer(serializers.ModelSerializer):
    onwer = serializers.ReadOnlyField(source ='job.onwer.username')
    class Meta:
        model = Job
        exclude = ('pkid',)
    
    
    def update(self, instance, validated_data):
        
        image = validated_data.get('image', None)
        if image is None:  
            validated_data['image'] = instance.image

        return super().update(instance, validated_data)
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
        
        
        
class ApplySerializer (serializers.ModelSerializer):
    class Meta:
        model = apply
        fields = '__all__'