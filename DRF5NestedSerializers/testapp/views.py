from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from testapp.serializers import AuthorSerailizer,BookSerailizer

from testapp.models import Author,Book

# Create your views here.

class AuthorLC(ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerailizer


class AuthorURD(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerailizer

class BookLC(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerailizer

class BookURD(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerailizer


