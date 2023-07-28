from django.contrib import admin

from .models import Canton, Contour, Region, District

admin.site.register(Canton)
admin.site.register(Contour)
admin.site.register(Region)
admin.site.register(District)

# Register your models here.
