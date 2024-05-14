from hpmode.models import Employee
from hpmode.models import Employee
from rest_framework import serializers

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'