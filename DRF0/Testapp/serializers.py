from rest_framework import serializers

from Testapp.models import Employee

def sal_mul_of_100(value): #validators(in built) used in esal column (line no 14)

    if value%100!=0:
        raise serializers.ValidationError('sal should be multiples of 100')
    
    return value


class EmployeeSerializer(serializers.ModelSerializer):  #model serailiser is same as normal serailiser except that its a shortcut and does not require to explicitly specify create and update methods
    #esal=serializers.FloatField(validators=[sal_mul_of_100])
    class Meta:
        model=Employee
        fields='__all__'
        #fields=['ename','eadr','eno'] #if you want to specify only some fields
        #exclude=['esal'] #if you want to exclude salary field


    # def validate_esal(self,value):  #field level validation..to force validation on only one field...function name should start with validate_<<field>>
    #     if value<5000:
    #         raise serializers.ValidationError('Employee sal should be min 5000.')
    #     return value


# class EmployeeSerializer(serializers.Serializer):  #Normal serializers
#     eno=serializers.IntegerField()
#     ename=serializers.CharField(max_length=64)
#     esal=serializers.FloatField(validators=[sal_mul_of_100]) #calling the above function as argument to validator
#     eadr=serializers.CharField(max_length=64)


#     def validate_esal(self,value):  #field level validation..to force validation on only one field...function name should start with validate_<<field>>
#         if value<5000:
#             raise serializers.ValidationError('Employee sal should be min 5000.')
#         return value

#     def validate(self,data): #object level validation..to enforce validation on multiple fields..function name should be 'validate'
        
#         eadr=data.get('eadr')
#         esal=data.get('esal')

#         if eadr.lower()=='vuyyuru':
#             if esal<15000:
#                 raise serializers.ValidationError("salary from address vuyyuru should be minimum 15000")
        
#         return data



#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data) #with all key,value pairs


#     def update(self,instance,validated_data): #validated data is partner app provided data

#         instance.eno=validated_data.get('eno',instance.eno)  #if eno is provided ..it takes the validated_data eno ...else it takes instance eno. value only
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eadr=validated_data.get('eadr',instance.eadr)

#         instance.save()

#         return instance

