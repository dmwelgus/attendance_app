
from django.db import models
from django.urls import reverse


class client(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=40)
    zip_code = models.IntegerField()

    class Meta:
        unique_together = ("first_name", "last_name", "birth_date")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('clients')


class programs(models.Model):

    program = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.program

    def get_absolute_url(self):
        return reverse('programs')


class sessions(models.Model):

    program = models.ForeignKey('programs', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


class attendance_log(models.Model):

    client = models.ForeignKey('client', on_delete=models.CASCADE)
    session = models.ForeignKey('sessions', on_delete=models.CASCADE)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('programs')
