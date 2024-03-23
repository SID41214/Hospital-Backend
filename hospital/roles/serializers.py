from rest_framework import serializers
from .models import User,Doctor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_doctor'] = user.is_doctor
        token['is_admin'] = user.is_admin
        token['is_active'] =user.is_active
        return token

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         try:
#             # Call the parent class method to get the token
#             token = super().get_token(user)
#             # Add custom claims to the token
#             token['username'] = user.username
#             token['is_doctor'] = user.is_doctor
#             token['is_admin'] = user.is_admin
#             token['is_active'] = user.is_active
#             return token
#         except AttributeError:
#             # Handle cases where user object does not have expected attributes
#             return None


class UserRegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email', 'password','password2','phone_number','avatar','is_doctor']
        
        
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
        
        

class UserProfileSerializer(serializers.Serializer):
    doctor_profile =DoctorProfileSerializer(allow_null =True,required=False)
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','avatar','doctor_profile']       
        


class DoctorListSerializer(serializers.ModelSerializer):
    doctor = DoctorProfileSerializer(source='doctors',many=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_number','avatar','doctor']
        
        

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','username','first_name','last_name','email','is_active','is_admin','blocked','is_doctor','is_staff']


    






















