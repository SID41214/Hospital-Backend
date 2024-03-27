
from django.contrib import admin
from django.urls import path,include
from roles import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



# router = DefaultRouter()
# router.register('register',views.Registration,basename='register') 

# router = DefaultRouter()
# router.register('userslist',views.UserListView,basename='userslist') 





urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls)),
    path('register/',views.Registration.as_view(),name='register'),
    path('login/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userslist/',views.UserListView.as_view(),name='userslist'),
    path('doctorlist/',views.UserDoctorView.as_view(),name = 'doctorlist'),
    path('userprofile/',views.UserProfileView.as_view(),name = 'profile'),
    path('adminuserlist/',views.AdminView.as_view(),name='adminuserlist'),
    path('adminuserlist/<int:pk>/',views.AdminView.as_view(),name='adminuserlist'),


]
















