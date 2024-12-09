from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()
    image = models.ImageField(upload_to='hall_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    department_name = models.CharField(max_length=100)
    event_name = models.CharField(max_length=200)
    num_students = models.IntegerField()
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
        from django.db import models

class Booking(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_students = models.IntegerField()
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event_name} on {self.event_date}"




