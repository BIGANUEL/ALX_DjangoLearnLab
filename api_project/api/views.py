from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
