from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.

DISTANCE_UNITS_CHOICES = [
    ('km', 'km'),
    ('mile', 'mile'),
    ('m', 'm'),
]

EVENT_UNITS_CHOICES = [
    ('800m', '800m'),
    ('1500m', '1500m'),
	('1mile', '1mile'),
    ('3000m', '3000m'),
    ('3000mSC', '3000mSC'),
    ('2mile', '2mile'),
    ('5000m', '5000m'),
    ('10000m', '10000m'),
    ('ハーフマラソン', 'ハーフマラソン'),
    ('フルマラソン', 'フルマラソン'),
]

class Admin(models.Model):
    email = models.EmailField(unique=True)
    login_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    admin_name = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not check_password(self.password, self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.admin_name

class User(models.Model):
    email = models.EmailField(unique=True)
    login_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    user_name = models.CharField(max_length=20)

    distance_value = models.FloatField(null=True, blank=True)
    distance_unit = models.CharField(max_length=5, choices=DISTANCE_UNITS_CHOICES, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    elevation = models.IntegerField(null=True, blank=True)
    temperature = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not check_password(self.password, self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.user_name

class Specialty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=20, choices=EVENT_UNITS_CHOICES, null=True, blank=True)
    best_time = models.CharField(max_length=11, null=True, blank=True, help_text="Time in the format hh:mm:ss:SS")

    def __str__(self):
        return self.event_name