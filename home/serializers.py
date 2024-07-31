from rest_framework import serializers
from django.contrib.auth.models import User




class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('This username is already taken')
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('This email is registered to another account')
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data














# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         if User.objects.filter(username=data['username']).exists():
#             raise serializers.ValidationError('This username is already taken')
        
#         if User.objects.filter(email=data['email']).exists():
#             raise serializers.ValidationError('An account already registered with this email')
        
#         return data
    
#     def create(self, validated_data):
#         user = User.objects.create(username=validated_data['username'], email= validated_data['email'], first_name=validated_data['first_name'],last_name=validated_data['last_name'],  )
#         user.set_password(validated_data['password'])
#         user.save()
#         return validated_data
    


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()