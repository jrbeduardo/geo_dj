from django.contrib import admin
from .models import Visitor, Measurement

# Register your models here.

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'latitud', 'longitud')
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
