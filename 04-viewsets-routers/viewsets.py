from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter

from serializers import Book, BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


router = DefaultRouter()
router.register("books", BookViewSet, basename="book")
urlpatterns = router.urls