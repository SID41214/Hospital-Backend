from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,phone_number,
                    password=None,password2=None,is_doctor=False):
        if not email:
            raise ValueError("Please enter an email address")
        user =self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=phone_number,
            is_doctor=is_doctor,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,phone_number,password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=phone_number,
            password=password,
            )
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    email=models.EmailField(unique=True,max_length=250)
    phone_number =models.CharField(max_length=10,unique=True)
    blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar =models.ImageField(upload_to='avatars/',null=True,blank=True)

    objects=UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name', 'username','phone_number']
    
    def __str__(self):
        return f'{self.email} -- ({self.username})'
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        """
        Return True if the user has any permissions in the given app label.
        Simplest possible answer: Yes, always, as this user model does not use app-level permissions.
        """
        # "Does the user have permissions to view the app `app_label`?"
        return True
    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     #  All admins are staff
    #     return self.is_admin
        
    

STATUS_CHOICES = (
    ('Available', 'Available'),
    ('On Rounds', 'On Rounds'),
    ('Unavailable', 'Unavailable'),
    ('On Call', 'On Call'),
    ('In Surgery', 'In Surgery'),
    ('On Leave', 'On Leave'),
    ('Emergency', 'Emergency'),
)
class Doctor(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctors')
    department=models.CharField(max_length=255,null=True, blank=True)
    hospital = models.CharField(max_length=255, null=True,blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    
    is_verified = models.BooleanField(default=False)
    































































