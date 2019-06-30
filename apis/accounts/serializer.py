from rest_framework.serializers import ModelSerializer
from django.conf import settings
from apis.accounts.models import User, Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model=profile   
        field='__all__'


class CreateUserSerializer(ModelSerializer): 
    profile_Serializer =ProfileSerializer()
     
    class Meta:
        model=User
        Field=('email','first_name','last_name','password')

    def create(self, validated_data):
        profile_data=validated_data('profile')