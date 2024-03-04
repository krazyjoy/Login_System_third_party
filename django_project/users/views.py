from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .models import TestUser

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        user = None
        token = None
        # check if username is set up as email
        if '@' in email:
            try:
                user = TestUser.objects.get(email=email)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password, email=email)

        if user:
            # check if remember token exists and  is not expired
            remember_token = user.remember_token
            if remember_token and user.remember_token_expiration > timezone.now():
                token = remember_token
            else:
                token, _ = Token.objects.get_or_create(user=user)
                user.remember_token = token.key
                expiration_time = timezone.now()+timedelta(days=2)
                user.remember_token_expiration = expiration_time
                user.save()
                remember_token = token.key


            response_user = {
                "token": remember_token,
                "user": {
                    'username': user.name,
                    'email': user.email,
                    'register_from': user.register_from,
                    'avatar': user.avatar,
                    'gender':user.gender,
                    'birthday': user.birthday,
                    'phone': user.phone,
                    'website': user.website,
                    'biography': user.biography,
                    'zipcode': user.zipcode,
                    'country': user.country,
                    'state': user.state,
                    'city':user.city,
                    'address': user.address
                }

            }


            return Response(response_user, status=status.HTTP_200_OK)

        return Response({'error':'Invalid Credentials'}, status = status.HTTP_401_UNAUTHORIZED)

def token_authentication(request):
    # extract token from request headers
    token_key = request.headers.get('Authorization').split(' ')[1]

    try:
        token = Token.objects.get(key=token_key)
        user = token.user
        return user

    except Token.DoesNotExist:
        return None

@api_view(['PUT'])
def update_user(request):
    user = None
    user = token_authentication(request)
    if user is None:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    error_keys = []
    updated_fields = request.data.keys()
    for field in updated_fields:
        if hasattr(user, field):
            setattr(user, field, request.data[field])
        else:
            error_keys.append(field)


    user.save()

    # Initialize not_existed variable
    not_existed = ""

    # Some code here that defines error_keys

    if error_keys:
        for error_key in error_keys:
            not_existed += error_key + ", "
        return Response({'message': f'error accessing keys: {not_existed}'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'User fields updated successfully'}, status=status.HTTP_200_OK)



@api_view(['PUT'])
def fake_delete_user(request):
    user = None
    user = token_authentication(request)
    if user is None:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    setattr(user, "deleted_at", timezone.now())
    user.save()
    return Response({'message':f'Successfully deleted user {user.name}'})
