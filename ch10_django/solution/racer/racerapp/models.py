from django.db import models


# Create your models here.
class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    race = models.ForeignKey('Race', on_delete=models.CASCADE, )

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.age)


class Race(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    distance = models.FloatField()

    def __str__(self):
        return '{0} ({1}'.format(self.name, self.location)
