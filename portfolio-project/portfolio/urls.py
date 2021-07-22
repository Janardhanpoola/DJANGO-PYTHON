
from django.contrib import admin
from django.urls import path
from django.conf import settings  #import settings
from django.conf.urls.static import static#import static
import jobs.views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home,name="home"),
    path('blog/',include('blog.urls')),  #the name inside include function should be the name of the app exactly
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #when users clicks on image it wont show the image.To enable this use this + static
