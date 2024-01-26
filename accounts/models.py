from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AccountManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
             raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            name = name
            )
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_author(self, name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password
        )
        user.is_author = True
        user.save(using = self._db)

        return user
    
    def create_superuser(self, name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password
        )
        user.is_superuser = True
        user.is_staff      = True
        user.is_active     = True
        user.save(using = self._db)

        return user



class Account(AbstractBaseUser, PermissionsMixin):
    name         = models.CharField(max_length=250)
    email        = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    is_active     = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_author     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined   = models.DateTimeField(auto_now_add=True)
    last_login    = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    



