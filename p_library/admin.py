from django.contrib import admin

from p_library.models import Book, Author, Publisher

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):

    @staticmethod
    def books_list(obj):
        return list(obj.published_books.all())

    list_display = ("name", "books_list")

