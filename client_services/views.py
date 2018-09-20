from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import client, programs, sessions
# from .forms import AttendanceForm


def home(request):

    return render(request, 'home.html')


def clients(request):
    clients = client.objects.all()
    return render(request, 'client.html', {'clients': clients})


def program_list(request):
    program_list = programs.objects.all()
    return render(request, 'programs.html', {'program_list': program_list})


def session_list(request):
    session_list = sessions.objects.all()
    return render(request, 'sessions.html', {'session_list': session_list})


def take_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendees = form.cleaned_data.get('attendees')

    else:
        form = AttendanceForm

    return render(request, 'take_attendance.html', {'form': form})


class new_clients(CreateView):

    model = client

    template_name = 'new_client.html'

    fields = '__all__'


class new_program(CreateView):

    model = programs

    template_name = 'new_program.html'

    fields = '__all__'


class new_session(CreateView):

    model = sessions

    template_name = 'new_session.html'

    fields = '__all__'

