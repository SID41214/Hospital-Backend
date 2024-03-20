from rest_framework import serializers
from .models import User,Doctor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer







class UserRegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email', 'password','password2','phone_number','is_doctor']
        
        
    def validate(self,data):
        username=data.get('username')
        password=data.get('password')
        password2=data.get('password2')
        phone_number=data.get('phone_number')
        is_doctor=data.get('is_doctor')
        
        if password != password2:
            raise serializers.ValidationError('Password Mismatch')
        
        if len(password)<8:
            raise serializers.ValidationError('Password contain aleast 8 characters')
        
        if len(phone_number)<10:
            raise serializers.ValidationError('Phone number must be of length 10')
        
        return data
    
    
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields=['department','hospital','status','is_verified']
        
        
        

























