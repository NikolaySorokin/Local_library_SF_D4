from django.contrib import admin

from p_library.models import Book, Author, Publisher, Friend


# Register your models here.
class MembershipInline(admin.TabularInline):
    model = Book.lend_to.through
    min_num = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('lend_to',)

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

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):

    @staticmethod
    def borrowed_books(obj):
        return list(obj.book_set.all())

    list_display = ("name", "borrowed_books")


