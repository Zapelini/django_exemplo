from django.contrib import admin

# Register your models here.
from dashboard.models import Client, Vehicle


class ClientAdmin(admin.ModelAdmin):
    pass


class VehicleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)
