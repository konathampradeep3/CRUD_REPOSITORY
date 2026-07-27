from django.contrib import admin

# Register your models here.
from healthcare.models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientDoctor)
