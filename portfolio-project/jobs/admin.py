from django.contrib import admin

from .models import Job #to show the apps(jobs) in admin page import job from models file

admin.site.register(Job)  #when you refresh /admin page,it will show image and summary to add jobs desired

