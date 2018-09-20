from django import forms
from .models import client, programs

clients = client.objects.all()
program_list = programs.objects.all()


class AttendanceForm(forms.Form):

    program_display = ((program_list[i], program_list[i]) for i in range(len(program_list)))
    client_display = ((clients[i], clients[i]) for i in range(len(clients)))

    program = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=program_display)

    attendees = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=client_display
    )
