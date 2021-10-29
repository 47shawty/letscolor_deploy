from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, password=None):
        if not phone_number:
            raise ValueError('User must have a phone_number')

        user = self.model(
            phone_number = phone_number,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, password):
        user = self.create_user(
            phone_number = phone_number,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50, verbose_name="First Name", null=True, blank=True)
    last_name       = models.CharField(max_length=50, verbose_name='Last Name', null=True, blank=True)
    phone_number    = models.CharField(max_length=50, unique=True, verbose_name='Phone Number')

    # required
    date_joined     = models.DateTimeField(auto_now_add=True, verbose_name='Data Joined')
    last_login      = models.DateTimeField(auto_now_add=True, verbose_name='Last Login')
    is_admin        = models.BooleanField(default=False, verbose_name='Is Admin')
    is_staff        = models.BooleanField(default=False, verbose_name='Is Staff')
    is_active        = models.BooleanField(default=True, verbose_name='Is Active')
    is_superadmin        = models.BooleanField(default=False, verbose_name='Is Superadmin')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name='User')
    address_line_1 = models.CharField(blank=True, max_length=100, verbose_name='Address Line 1')
    address_line_2 = models.CharField(blank=True, max_length=100, verbose_name='Address Line 2')
    profile_picture = models.ImageField(blank=True, upload_to='userprofile', verbose_name='Profile Picture')
    city = models.CharField(blank=True, max_length=20, verbose_name='City')
    state = models.CharField(blank=True, max_length=20, verbose_name='State')
    country = models.CharField(blank=True, max_length=20, verbose_name='Country')

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
