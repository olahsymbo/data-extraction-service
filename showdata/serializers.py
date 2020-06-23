from .models import Taskdata
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    '''
    create a django serializer to convert the raw data load from postgres DB
    to a well formatted type such as json.
    '''
    class Meta:
        model = Taskdata
        fields = ('id', 'timestamp', 'temperature', 'duration')