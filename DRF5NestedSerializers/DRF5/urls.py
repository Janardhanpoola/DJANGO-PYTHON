"""DRF5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from testapp.views import AuthorLC,AuthorURD,BookURD,BookLC

urlpatterns = [
    path('admin/', admin.site.urls),

    path('author-api/',AuthorLC.as_view()),

    re_path('^author-api/(?P<pk>\d+)/$',AuthorURD.as_view()),

    path('book-api/',BookLC.as_view()),

    re_path('^book-api/(?P<pk>\d+)/$',BookURD.as_view())
]
