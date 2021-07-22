from django.core.management.base import BaseCommand
import sqlite3
from Test.models import Track


class Command(BaseCommand):
    help='import booms'

    def add_arguments(self,parser):
        pass

    def handle(self,*args,**kwargs):
        
        conn=sqlite3.connect('chinook.db')
        c=conn.cursor()
        c.execute('select * from tracks')
        data=c.fetchall()

        for (TrackId,Name,AlbumId,MediaTypeId,GenreId,Composer,Milliseconds,Bytes,UnitPrice) in data:
            models=Track(id=TrackId,trackname=Name,Albumid=AlbumId,MediaTypeid=MediaTypeId,GenreId=GenreId,Composer=Composer,Milllisecs=Milliseconds,Bytes=Bytes,unitprice=UnitPrice)
            models.save()  #type python manage.py populate which helps to populate database

