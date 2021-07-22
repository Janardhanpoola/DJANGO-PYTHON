from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from testapp.models import Employee

from testapp.serializers import EmployeeModelSerializer

from rest_framework.authentication import TokenAuthentication  #library for specifying the type of authentication

from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,AllowAny

from testapp.permissions import ReadOnly,DeleteorPatch ,JanardhanPermission #custom permission class

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

##############################
#Default permission classes
#############################


class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeModelSerializer

#    authentication_classes=[TokenAuthentication] #specify the type of token you want to authenticate
# 1.   permission_classes=[IsAuthenticated]  #only authenticated users can access API
    #permission_classes=[AllowAny] #allow any user to access API 

# 3.   permission_classes=[IsAdminUser] #only admin users has permission to access data

# 4.    permission_classes=[IsAuthenticatedOrReadOnly]  #unauthorized users can get the data but cant do write operations and only the authorized users can read,write the data(post,get,put,patch)

##########djangomodelpermissions

#5.    permission_classes=[DjangoModelPermissions]  
 
 # a.only authenticated users can only get the data but cant do write operations(post,put,patch)

    #b. to perform write operations(authenticated users) model permissions need to be set for every operation

    #c. POST--> add model  ,delete--> delete model ,put,patch-->change model permissions

    #d. these permissions can be done at admin interface(user section user permissions at model level)

    #e. as an example ...chakri user(adminuser) can modify any user data based on the model permissions provided..

    #f. but jpoola being a superuser doesnt require any model permissions to write data of other users.
   
  #  permission_classes=[DjangoModelPermissionsOrAnonReadOnly] #same as DjangoModelPermissions except any user can perform read operation

    #if lines 20,21 are not provided anyone can access the api info..if provided  only authenticated users can access data
    # check http http://127.0.0.1:8000/api  in cmd prmpt..by commenting and uncommenting those lines


    # to get token..issue http http://127.0.0.1:8000/get-api-token username="janardhan" password="jana1212" in cmfd prompt

    #to get the details of authenticated users ..give http http://127.0.0.1:8000/api/ "authorization:Token 2f0d9e4ce84fae34b2b287942880b43dda892474"


    #if you want to get data from POSTMAN..mention key: Authorization   value: Token <<token>> in the headers section


    #we can specify authentication in 2 ways:

    #locally and globally

    #locally :authentication and permissions are  only to one CBV(lines 19,20)
    #globally (defined in settings.py): authentication and permissons are for all CBV's defined in views.py

##########you can give /api/1 to retrieve the first field


##three types of users:

#1.normal users: cant access admin interface
#2.admin user: can access admin ..cant modify the data
#3.superuser: can access and modify any data without explicitly mentioning


#####################################################
# Custom permissions
########################################################


# first define the permissions in permission.py file

    #permission_classes=[ReadOnly]  
    #permission_classes=[DeleteorPatch]
    #permission_classes=[JanardhanPermission]


#####
# Drawback of Token authentication:

# for every request there is a request from and to the database and DRF to get the user associated with the token
# therfore,scalaility ..performance problems.. as no. of requests will b more

##JWT AUTHENTICATION
#Hence, 3rd party tokens is the solution ..i.e. JWT(Json web token authentication)

#need to do pip install djangorestframework_jwt

#each token lifetime is 5 mins by default..and you need to provide un and pwd to create a new one after it expired

#  --> access token(to obtain a token )

#  --> refresh token (to create a brand new token for an existing token before its expiry )

#  -->verify token (to verify if token is valid)

# you can customise the default access token time(5 mins) to any time you want  in settings.py line 64

#you can customise the default refresh token time(7 days ) to any time you want in settings.py line 65

    authentication_classes=[JSONWebTokenAuthentication] #make sure you send key: Authorization and value: JWT <token> in header sec. in POSTMAN and get the details of employee by issuing http://127.0.0.1:8000/api/
    permission_classes=[AllowAny]

