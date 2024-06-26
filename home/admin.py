from django.contrib import admin
from .models import userdata, availability
# Register your models here.
class userdataAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'passportNumber', 'citizenship', 'telephone', 'getEmail')
class availabilityAdmin(admin.ModelAdmin):
    list_display = ('url',)

admin.site.register(userdata, userdataAdmin)    

admin.site.register(availability, availabilityAdmin)    