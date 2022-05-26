from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.
class SMS_auth(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='smsauth') 
    phone_number = models.CharField(primary_key=True, max_length=11)
    time_stamp = models.IntegerField(default=0)
    auth_number = models.IntegerField(default=0)
    is_auth = models.BooleanField(default=False)


class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11, default=0)
    profile_image = models.IntegerField(
        default = 0,
        validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ]
    )
