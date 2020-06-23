from django.db import models


class Taskdata(models.Model):
    '''
    create a Taskdata model as an ORM to access the corresponding
    data table in our postgres DB.

    define each column: id, timestamp, temperature, duration with the proper data types
    '''
    class Meta:
        db_table = 'taskdata'

    id = models.IntegerField(primary_key=True)

    timestamp = models.DateTimeField()

    temperature = models.CharField(max_length=250)

    duration = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.id} {self.timestamp} {self.temperature} {self.duration}"
