from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Book
        fields = ('title', 'isbn',
                 'pageCount', 
                 'publishedDate', 
                 'thumbnailURL', 
                 'shortDescription',
                 'longDescription',
                 'status',
                 'authors',
                 'categories',
                 )
