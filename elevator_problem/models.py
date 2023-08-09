from django.db import models

# Create your models here.

class Elevator(models.Model):

    STATE_CHOICES = [
        ('up', 'Up'),
        ('down', 'Down'),
        ('stop', 'Stop'),
    ]

    DOOR_CHOICES = [
        ('open','Open'),
        ('close',"Close")
    ]
    id = models.AutoField(primary_key=True)
    door_status = models.CharField(choices=DOOR_CHOICES, default="close", max_length=5)
    max_floor = models.IntegerField(default = 5)
    min_floor = models.IntegerField(default=0)
    current_floor = models.IntegerField(default=1)
    state = models.CharField(max_length=5, choices=STATE_CHOICES, default='stop')
    is_operational = models.BooleanField(default=True)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return f'Elevator ID: {self.id}'

class ElevatorRequest(models.Model):
    REQUEST_CHOICES = [
        ('pending','Pending'),
        ('complete', 'Complete')
    ]
    id = models.AutoField(primary_key=True)
    lift_id = models.ForeignKey(to=Elevator, on_delete=models.CASCADE, editable=False)
    requested_floor = models.IntegerField()
    request_status = models.CharField(choices=REQUEST_CHOICES, default="pending", max_length=8)