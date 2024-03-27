from rest_framework import serializers
from .models import User,Doctor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_doctor'] = user.is_doctor
        token['is_admin'] = user.is_admin
        token['is_active'] =user.is_active
        token['blocked'] = user.blocked
        return token
    
    def validate(self,attrs):
        data=super().validate(attrs)
        user=self.user
        password=attrs.get('password')
        # print(password,'its password')
        # print(user.password,'its next')
        
        if user.blocked:
            print(user,'blocked')
            raise AuthenticationFailed("Your account is blocked due to some reason, please contact admin")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        
        return data
            

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
        email = data.get('email')
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
    
    def validate_email(self, value):
       
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address is already in use.')
        return value    
    
    
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields=['department','hospital','is_verified']
        
    # Assuming you're trying to serialize a single Doctor instance
        
        

# class UserProfileSerializer(serializers.Serializer):
#     # doctor_profile =DoctorProfileSerializer(allow_null =True,required=False)
#     doctors =
#     class Meta:
#         model=User
#         fields = ['first_name','last_name','username','email','avatar','doctor_profile']       
    
class UserListSerializer(serializers.ModelSerializer):
    doctors = DoctorProfileSerializer(many=True, read_only=True) # Use many=True to handle multiple doctors
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','doctors']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        

        if instance.is_doctor:
            print(instance,'insta')
            doctorProfile = validated_data.get('doctors')
            print(doctorProfile,"prtjfhuhsi")
            if doctorProfile:
                doctor,created = Doctor.objects.get_or_create(user=instance) # pylint: disable=no-member
                doctor.hospital = doctorProfile.get('hospital',doctor.hospital)
                doctor.department = doctorProfile.get('department',doctor.department)
                doctor.save()
        instance.save()
        return instance 


class DoctorListSerializer(serializers.ModelSerializer):
    doctor = DoctorProfileSerializer(source='doctors',many=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_number','avatar','doctor']
        
        

class AdminSerializer(serializers.ModelSerializer):
    doctor = DoctorProfileSerializer(source='doctors')
    class Meta:
        model = User
        fields = ['pk','username','first_name','last_name','email','is_active','is_admin','blocked','is_doctor','is_staff','doctor']


    






















