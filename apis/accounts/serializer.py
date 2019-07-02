from rest_framework.serializers import ModelSerializer
from django.conf import settings
from apis.accounts.models import User, Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile   
        # fields='__all__'
        exclude=('dob', 'user')





class UserSerializer(ModelSerializer): 
    profile =ProfileSerializer()
     
    class Meta:
        model=User 
        fields=('email','username','first_name','last_name','password','profile')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        profile_data=validated_data.pop('profile')
        raw_password=validated_data.pop('password') 
        user=User(**validated_data)
        user.set_password(raw_password)
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validate_data):
        profile_data=validate_data.get('profile')
        profile_instance=Profile.objects.get(user=instance)
        instance.first_name=validate_data.get('first_name', instance.first_name)
        instance.last_name=validate_data.get('last_name', instance.last_name)
        if validate_data.get('password'):
            instance.set_password(validate_data.get('password'))
        instance.save()    
        profile_instance.address=profile_data.get('address',profile_instance.address)
        profile_instance.save()
        return instance