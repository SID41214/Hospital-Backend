from django.contrib import admin
from roles.models import User,Doctor

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','phone_number','is_doctor']
    

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['id','user','department','hospital','status']





