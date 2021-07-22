from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer

from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
# 1.Basicauthentication

    #authentication_classes=[BasicAuthentication,] # this provides a pop up to enter credentials on the screen
                                                  #this is not secure since it has credentials are in base64 encoding
                                                  #we cant control the auth. form

    #http http://127.0.0.1:8000/api/ "authorization:Basic anBvb2xhOjEyMw=="  ..issue in cmnd prompt to get the encoded msg in base64 encoding online by providing jpoola:123"
    
#2. SessionAuthentication
    authentication_classes=[SessionAuthentication,] #this is DRF default auth class...logout from django-admin.. try accessing the url..it shows auth details not provided
                                                    #for session auth..you need to login using a form provided by auth app
                                                    # to do this...1)add auth app urls in urls.py(line 31 in urls.py)
                                                    #2). go to browser and issue http://127.0.0.1:8000/accounts/login/ it shows template doesnt exists
                                                    #3) add a login.html and create login form in templates
                                                    #4)specify LOGIN_REDIRECT_URL in settings.py for the form to redirect to the api/..line 85 in settings.py
                                                    #5) if you want to logout use ...http://127.0.0.1:8000/accounts/logout/

    permission_classes=[IsAuthenticated,]


