from django.contrib import admin
from .models import Company, Drivers, Users, Trips

admin.site.register(Company)
admin.site.register(Drivers)
admin.site.register(Users)
admin.site.register(Trips)

# Register your models here.
