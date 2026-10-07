from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from serializers import Book, BookSerializer


class BookPagination(PageNumberPagination):
    page_size = 10


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]