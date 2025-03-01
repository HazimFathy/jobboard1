from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    country = CountryField(source = 'profile.country')
    phone_number = PhoneNumberField(source = 'profile.phone_number')
    city = serializers.CharField(source = 'profile.city')
    gender = serializers.CharField(source = 'profile.gender')
    profile_photo = serializers.ImageField(source = 'profile.profile_photo')
    
    class Meta :
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'country',
            'city',
            'gender',
            'phone_number',
            'profile_photo',
        ]