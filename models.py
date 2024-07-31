from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hospital_images/')
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, related_name='doctors', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='doctor_images/')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_contact = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.patient_name} - {self.hospital.name}"
