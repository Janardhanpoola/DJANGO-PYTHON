from rest_framework.serializers import ModelSerializer
from testapp.models import Author,Book



class BookSerailizer(ModelSerializer): #secondary serializer dependent on first
    class Meta:
        model=Book
        fields='__all__'

class AuthorSerailizer(ModelSerializer):  #primary serializer

    books_by_author=BookSerailizer(read_only=True,many=True)  # NESTED SERAIALIZER CONCEPT ..using one serializer inside another..defining books info by author.
                                                            # read_only we can only print book info cant modify it
                                                            # many is one author can have multiple books 


    class Meta:
        model=Author
        fields='__all__'