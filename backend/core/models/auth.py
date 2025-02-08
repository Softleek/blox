# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.utils import timezone
from .template import BaseModel



class RoleType(BaseModel):
    name = models.CharField(max_length=255)
    
class Branch(BaseModel):
    name = models.CharField(max_length=255)
    
    
class User(AbstractUser):
    ROLE_CHOICES = (
        ("Customer", "Customer"),
        ("Staff", "Staff"),
        ("Admin", "Admin"),
    )

    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default="Customer")
    groups = models.ManyToManyField(
        Group, related_name="api_user_groups", blank=True  # Add a unique related name
    ) 
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="api_user_permissions",  # Add a unique related name
        blank=True,
    )
    profile_picture = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    last_activity = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        # Check the role and set is_superuser and is_staff accordingly
        if self.role == 'Admin':
            self.is_superuser = True
            self.is_staff = True
        elif self.role == 'Staff':
            self.is_superuser = False
            self.is_staff = True
        else:  # customer or any other role
            self.is_superuser = False
            self.is_staff = False

        # Call the parent class's save method to save the changes
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)


class UserIPAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ip_addresses')
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'ip_address')

    def __str__(self):
        return f"{self.user.username} - {self.ip_address} ({self.timestamp})"