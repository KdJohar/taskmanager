from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task

        fields = ('id', 'name','user', 'deadline_date', 'completed', 'description', 'date_added', )
