from .models import Customer

from django.contrib.auth.models import User,Group

from django.db.models.signals import post_save

#remember to add ready method in apps.py and settings.py appconfig
def customer_profile(sender,instance,created,**kwargs): #sender is 'User'..instance is the user..created default is true
    if  created: #if profile is registered

        group=Group.objects.get(name='customer')#we want registered users to be a part of customer group..so getting the group named customer

        instance.groups.add(group) #adding the user to customer group

        Customer.objects.create(user=instance,name=instance.username)  #assigning  customer a user profile(user) as and when registered

        print('profile created')

post_save.connect(customer_profile,sender=User) #(receiver,sender)