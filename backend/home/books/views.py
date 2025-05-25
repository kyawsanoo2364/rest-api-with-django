from rest_framework import generics, filters
from .serializer import BookSerializer
from .models import Book
from . import permissions


# Create your views here.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def perform_create(self, serializer):
        user = self.request.user
        if user:
            serializer.save(author=user)

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            return qs.filter(author=user)
        return qs


class BookDetailsView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class BookUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsOwner]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsOwner]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


book_details_view = BookDetailsView.as_view()
book_update_view = BookUpdateView.as_view()
book_delete_view = BookDeleteView.as_view()
