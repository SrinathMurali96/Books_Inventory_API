from django.db import models

class Book (models.Model):
    book_id = models.AutoField('Book ID', db_column='BOOK_ID', primary_key=True)
    book_name = models.CharField('Book Name', db_column='BOOK_NAME',max_length=100)
    author = models.CharField('Author', db_column='AUTHOR',max_length=100)
    book_count = models.IntegerField('Book Count', db_column='BOOK_COUNT', default=1)

    class Meta:
        db_table = 'REF_BOOK'
        
        
class BookBorrowed(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_name = models.CharField('Book Name', db_column='BOOK_NAME',max_length=100)
    user = models.CharField('User Name', db_column='USERNAME',max_length=100)
    date_borrowed = models.DateTimeField('Borrowed Date', db_column='BORROWED_DATE')
    
    class Meta:
        db_table = 'REF_BORROWED'