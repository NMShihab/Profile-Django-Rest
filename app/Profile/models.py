from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin,BaseUserManager



class UserProfileManager(BaseUserManager):
    """Manager for User Profile"""
    def create_user(self,email,name,password=None):
        """Create a new User Profile"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_super_user(self,email,name,password):
        """Create Super User"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive Full Name"""
        return self.name

    def get_short_name(self):
        """Retrive short name"""
        return self.name

    def __str__(self):
        """Return String representation of User"""
        return self.email

