from django.urls import path
from .views import BookListView, book_details_view, book_update_view, book_delete_view

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<int:pk>/", book_details_view, name="book_details"),
    path("<int:pk>/update", book_update_view, name="book_update"),
    path("<int:pk>/delete", book_delete_view, name="book_delete"),
]
