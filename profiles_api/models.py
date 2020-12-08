from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for user Profiles"""

    def create_user(self, email, name, password= None):
        """Create a new user Profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)   # create a model object for email and name

        user.set_password(password) # make the password encripted

        user.save(using=self._db)

    def create_superuser(self, email, name, password):
        """Create and save a new Superuser with given details"""
        user = self.create_user(email, name, password=True) # creating user using create_user function

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #active users can log in
    is_staff = models.BooleanField(default=False)
    """
    Okay finally we need to specify the string representation of our model now this is the item
    that we want to return when we convert a user profile object to a string in
    Python you do that by typing
    """

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    def ___str___(self):
        """Return string representation of our user"""
        return self.email
