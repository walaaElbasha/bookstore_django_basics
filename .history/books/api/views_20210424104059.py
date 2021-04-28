#from django 
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer


def index(request):
    books = Book.object.objects.all()
    serializer=BookSerializer(instance=books,many=True)
    return Response(data=serializer.data,status=status_HTTP_200_ok)