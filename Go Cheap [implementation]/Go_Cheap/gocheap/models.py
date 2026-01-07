from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Company(models.Model):
    CompanyID = models.AutoField(primary_key=True)  # SQLite AutoField بدل INT
    CompanyName = models.CharField(max_length=50)

    def __str__(self):
        return self.CompanyName


class Drivers(models.Model):
    DriverID = models.AutoField(primary_key=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="drivers")
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    CarModel = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class Trips(models.Model):
    TripID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Driver = models.ForeignKey(Drivers, on_delete=models.CASCADE, related_name="trips")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="trips")
    User = models.ForeignKey(Users, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="trips")
    PickupArea = models.CharField(max_length=50)
    DropoffArea = models.CharField(max_length=50)
    DistanceKM = models.FloatField()
    Price = models.FloatField()
    TripDurationMin = models.IntegerField()

    def __str__(self):
        return f"Trip {self.TripID} by {self.Driver.Name}"

# Create your models here.
