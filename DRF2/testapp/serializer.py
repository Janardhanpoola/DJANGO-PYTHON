from rest_framework.serializers import ModelSerializer

from testapp.models import EmployeeInfo


class EmployeeModelSerializer(ModelSerializer):
    
    class Meta:
        model=EmployeeInfo
        fields='__all__'