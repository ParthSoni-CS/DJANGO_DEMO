from django.contrib import admin
from .models import flight,airport,passengers

admin.site.register(flight)
admin.site.register(airport)
admin.site.register(passengers)

# Register your models here.
