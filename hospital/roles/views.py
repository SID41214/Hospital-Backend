
















































# from django.shortcuts import render
# from rest_framework.views import APIView
# from roles.serializers import UserRegisterSerializer,MyTokenObtainPairSerializer,UserProfileSerializer,DoctorProfileSerializer,DoctorListSerializer,AdminSerializer
# from roles.models import User,Doctors
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.decorators import permission_classes
# from rest_framework.generics import ListAPIView



# # Create your views here.

# class Registration(APIView):

#     def post(self,request,format = None):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():

#             first_name=serializer.validated_data.get('first_name')
#             last_name=serializer.validated_data.get('last_name')
#             username=serializer.validated_data.get('username')
#             email=serializer.validated_data.get('email')
#             password=serializer.validated_data.get('password')
#             is_doctor=serializer.validated_data.get('is_doctor')

#             user = User.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#                 email=email,
#                 password=password,
#                 is_doctor=is_doctor
#             )
#             if user.is_doctor:
#                 Doctors.objects.create(user=user)
#             return Response({'msg':'data inserted'},status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
    



# class UserProfileView(APIView):
  
#     authentication_classes =[JWTAuthentication]
#     permission_classes = [IsAuthenticated]


#     def get(self, request):
#         user = request.user

#         if user.is_doctor:
#             try:
#                 doctor_profile = Doctors.objects.get(user=user)
#                 data = {
#                     'username': user.username,
#                     'first_name': user.first_name,
#                     'last_name': user.last_name,
#                     'email': user.email,
#                     # 'phone': user.phone,
#                     'is_doctor':user.is_doctor,
#                     'doctor_profile': {
#                         'hospital': doctor_profile.hospital,
#                         'department': doctor_profile.department,
#                         'is_verified': doctor_profile.is_verified,
#                     }
#                 }
#                 return Response(data, status=status.HTTP_200_OK)
#             except Doctors.DoesNotExist:
#                 return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             try:
#                 user_serializer = UserProfileSerializer(user)
#                 return Response(user_serializer.data, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
            

#     def patch(self, request):
#         try:
#             print(request.data)
#             user = request.user
#             if user.is_doctor:
#                 doctor_profile = Doctors.objects.get(user=user)
#                 doctor_serializer = DoctorProfileSerializer(doctor_profile, data=request.data, partial=True)

#                 if 'first_name' in request.data:
#                     user.first_name = request.data['first_name']
#                 if 'last_name' in request.data:
#                     user.last_name = request.data['last_name']
#                 user.save()  
                  
#                 if doctor_serializer.is_valid():
#                     doctor_serializer.save()
#                     return Response(doctor_serializer.data, status=status.HTTP_200_OK)
#                 else:
#                     return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 user_profile = User.objects.get(id=request.user.id)
#                 serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)

#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_200_OK)

#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except User.DoesNotExist:
#             return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#         except Doctors.DoesNotExist:
#             return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    
#     def delete(self, request):
#         user = request.user

#         if user.is_doctor:
#             try:
#                 doctor_profile = Doctors.objects.get(user=user)
#                 doctor_profile.delete()
#                 return Response({'detail': 'Doctor profile deleted.'}, status=status.HTTP_204_NO_CONTENT)
#             except Doctors.DoesNotExist:
#                 return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             try:
#                 user_profile = User.objects.get(id=user.id)
#                 user_profile.delete()
#                 return Response({'detail': 'User profile deleted.'}, status=status.HTTP_204_NO_CONTENT)
#             except User.DoesNotExist:
#                 return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
            

# class UserDoctorView(APIView):
#     def get(self, request):
#         doctors = User.objects.filter(is_doctor=True)
#         serializer = DoctorListSerializer(doctors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    


# class AdminView(APIView):
#     permission_classes = [IsAdminUser]
#     def get(self,request):
#         user = User.objects.all()
#         print(user)
#         serializer = AdminSerializer(user,many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def patch(self, request, pk):
#         try:
#             user = User.objects.get(id=pk)
#             print(user)
#             user.is_active = not user.is_active 
            
#             user.save()
#             serializer = AdminSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        

# class UserListView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer