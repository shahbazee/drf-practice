from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from serializers import Book, BookSerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer