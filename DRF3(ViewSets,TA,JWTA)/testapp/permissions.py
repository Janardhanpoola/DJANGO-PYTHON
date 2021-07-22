from rest_framework.permissions import BasePermission,SAFE_METHODS


class ReadOnly(BasePermission): #user defined permission which does read only operations
    def has_permission(self,request,view):  #predefined method
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class DeleteorPatch(BasePermission): #this class allows only patch or delete operations
    def has_permission(self,request,view):
        allowed_methods=['PATCH','DELETE']
        if request.method in allowed_methods:
            return True
        else:
            return False

########
#write a permission class where :
# if emp is janardhan allow all the permissions
# if emp is not janardhan and emp has even letter chars allow SAFE_METHODS
#else dont allow any permission

class JanardhanPermission(BasePermission):
    def has_permission(self,request,view):

        username=request.user.username

        if username.lower()=='janardhan':
            return True

        elif username!='' and len(username)%2==0 and request.method in SAFE_METHODS:  #username return empty string when there is an unauthenticated user
            return True
        
        else:
            return False



