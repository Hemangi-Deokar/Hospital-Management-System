# from django.contrib import admin
# from .models import Hospital, Doctor, Appointment

# admin.site.register(Hospital)
# admin.site.register(Doctor)
# admin.site.register(Appointment)
from django.contrib import admin
from .models import Hospital, Doctor, Appointment

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'address')
    search_fields = ('name', 'address')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital', 'specialization', 'contact_number')
    search_fields = ('name', 'specialization', 'hospital__name')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'hospital', 'appointment_date', 'appointment_time')
    search_fields = ('patient_name', 'hospital__name')

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
