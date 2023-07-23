from django.contrib import admin
from .models import Admin, User, Specialty

# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Specialty)