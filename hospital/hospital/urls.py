

from django.contrib import admin
from django.urls import path
from roles import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Registration.as_view(),name='register'),
    path('login/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('doctorlist/',views.UserDoctorView.as_view(),name = 'doctorlist'),
    path('userprofile/',views.UserProfileView.as_view(),name = 'profile'),
    path('userlist/',views.AdminView.as_view(),name='userlist'),
    path('userlist/<int:pk>/',views.AdminView.as_view(),name='userlist'),
    path('userslist/',views.UserListView.as_view(),name='userslist'),


]
















