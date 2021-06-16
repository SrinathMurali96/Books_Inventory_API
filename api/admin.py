from .models import Book
from django.contrib import admin

# Creating views in django admin to add books
class AddBookAdmin(admin.BookAdmin):
    model = Book
    list_display = ['book_name', 'author', 'book_count']
    list_editable = ['book_name', 'author', 'book_count']
    list_filter = []
    list_per_page = 10
    
    
admin.site.register(Book, AddBookAdmin)

# Creating views in django admin to view all the books
class AllBooks(admin.BookAdmin):
    model = Book
    list_display = ['book_name']
    list_filter = []
    list_per_page = 20
    
    
admin.site.register(Book, AllBooks)