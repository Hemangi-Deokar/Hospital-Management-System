from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital, Appointment
from .forms import AppointmentForm

def home(request):
    return render(request, 'home.html')

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})

def hospital_detail(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'hospital_detail.html', {'hospital': hospital})

def make_appointment(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.hospital = hospital
            appointment.save()
            return redirect('hospital_detail', pk=hospital.pk)
    else:
        form = AppointmentForm()
    return render(request, 'make_appointment.html', {'form': form})
