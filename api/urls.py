from django.conf.urls import url

from api.views import user_creation, login, borrow_book, get_borrowed_book

urlpatterns = [
    url(r'^services/userCreation', user_creation, name='userCreation'),
    url(r'^services/login/$', login, name='login'),
    url(r'^services/borrowBook' ,borrow_book , name='borrow_book'),
    url(r'^services/getBorrowed_book' ,get_borrowed_book , name='get_borrowed_book'),
]
