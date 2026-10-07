from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from serializers import Book, BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, 
                        OrderingFilter]
    filterest_fields = ["price", "author"]
    search_fields = ["title", "author"]
    Ordering_fields = ["price", "published"]