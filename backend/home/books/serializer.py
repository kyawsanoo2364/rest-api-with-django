from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="book_details", lookup_field="pk"
    )

    class Meta:
        model = Book
        fields = ("title", "description", "author", "url", "created_at")
