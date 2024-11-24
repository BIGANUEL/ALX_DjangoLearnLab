from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    