import logging
import traceback
LOGGER = logging.getLogger(__name__)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import F
from .models import Book,BookBorrowed
from rest_framework import authentication
from rest_framework import exceptions

"""
API: Creating the User
"""
@csrf_exempt
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def user_creation(request):
    LOGGER.info('Register / Create a user API Method - Starts')
    data = {}
    try:
        # Getting the input from the user
        name = request.data["Name"]
        email = request.data["Email"]
        password = request.data["Password"]
        
        # Checking if input has all the values to create user
        if name and email and password:
            
            # Checking if user is already present in the database
            if User.objects.filter(username=name,email = email).exists():
                data['status'] = 'Warning'
                data['message'] = 'User already Exists'
            
            # User creation and storing the values in database
            else:
                user = User.objects.create_user(name, email,password)
                
                # Sending the success status as the user is created
                data['status'] = 'Success'
                data['message'] = user + ' created Successfully'
        
        # Setting status as Failed since required values are not present
        else:
            data['status'] = 'Failed'
            data['message'] = 'Please enter required values'
              
    except Exception:
        LOGGER.error(traceback.format_exc())
        data['status'] = 'Failed'
        data['message'] = 'Error while creating user'
        
    LOGGER.info("Sent data: {}".format(data))
    LOGGER.info('Register / Create a user API Method - Ends')
    return Response(data)


"""
API: Login API
"""
@csrf_exempt
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def login(request):
    LOGGER.info('Login API Method - Starts')
    data = {}
    try:
        
        # Getting the input from the user
        email = request.data["Email"]
        password = request.data["Password"]
        
        # Checking if input has all the values to create user
        if email and password:
            
            # User validation 
            user = authenticate(email = email, password='secret')
            if user is not None:
                data['status'] = 'Failed'
                data['message'] = 'Email / Password is incorrect'
            else:
                data['status'] = 'Success'
                data['message'] = 'Login Successful'
                request.session['user_name'] = user
    except Exception:
        LOGGER.error(traceback.format_exc())
        data['status'] = 'Failed'
        data['message'] = 'Error while Login'
        
    LOGGER.info("Sent data: {}".format(data))
    LOGGER.info('Login API Method - Ends')
    return Response(data)

"""
API: Borrow Book API
"""
@csrf_exempt
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def borrow_book(request):
    LOGGER.info('Borrow Book API Method - Starts')
    data = {}
    try:
        
        # Performing the authentication
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None
        
        # Getting the input from the user
        book_id = request.data["book_id"]
        Date = request.data["Date"]
        
        # Reducing the count of given book_id by 1
        book_obj = Book.objects.get(book_id = book_id)
        book_obj.book_count = F('book_count') - 1
        book_obj.save()
        
        # Updating the value in Book Borrowed model
        borrow_obj = BookBorrowed()
        borrow_obj.book_id = book_id
        borrow_obj.user = request.session['user_name']
        borrow_obj.date_borrowed = Date 
        borrow_obj.book_name = book_obj.book_name 
        borrow_obj.save()
        
        data['status'] = 'Success'
        data['message'] = 'Updated Borrowed Book'
        
    except Exception:
        LOGGER.error(traceback.format_exc())
        data['status'] = 'Failed'
        data['message'] = 'Error while updating book'
        
    LOGGER.info("Sent data: {}".format(data))
    LOGGER.info('Borrow Book API Method - Ends')
    return Response(data)   
            
@csrf_exempt
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_borrowed_book(request):
    LOGGER.info('Get Borrowed Book API Method - Starts')
    data = {}
    try:
        user = request.data["user"]
        borrowed_list = BookBorrowed.objects.filter(user = user).values_list('book_name', flat=True)
        
        data['status'] = 'Success'
        data['Borrowed Books'] = borrowed_list
        
    except Exception:
        LOGGER.error(traceback.format_exc())
        data['status'] = 'Failed'
        data['message'] = 'Error while fetching books details'
        
    LOGGER.info("Sent data: {}".format(data))
    LOGGER.info('Get Borrowed Book API Method - Ends')
    return Response(data)