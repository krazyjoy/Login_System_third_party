from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import TestUser

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# update function
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json

# user blocked articles
from rest_framework import generics
from articles.serializer import ArticleSerializer


from articles.models import Articles
from .forms import CustomSignupForm
from django.contrib import messages

from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import TestUser
from django.shortcuts import render
from .forms import CustomUserUpdateForm
def home(request):
    model_fields = TestUser._meta.get_fields()

    # Extract field names and their types
    field_info = [(field.name, field.get_internal_type()) for field in model_fields]

    # print(field_info)
    context = {
        'users': TestUser.objects.all()
    }
    print(f'context: {context}')
    return render(request, 'users/account_base.html', context)


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow access to unauthenticated users
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

            if remember_token is None or (
                    user.remember_token_expiration is not None and user.remember_token_expiration < timezone.now()):
                token, _ = Token.objects.get_or_create(user=user)
                remember_token = token.key
                user.remember_token = remember_token
                # expiration_time = timezone.now() + timedelta(days=2)
                user.save()

            # return user dictionary object
            user_serializer = UserSerializer(user)
            user_data = user_serializer.data
            response_user = {
                "token": remember_token,
                "user": user_data
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
        # user_data = serializers.serialize('json', [user, ])
        user_serializer = UserSerializer(user)
        user_data = user_serializer.data
        #user_data_in_json = json.dumps(user_data, cls=DjangoJSONEncoder)
        print("user_data", user_data)
        try:
            block_ids = []

            if 'block' in user_data.keys():
                # store article data in a dictionary, with key as article id
                article_data = {}
                # for key in [1,2,3]:
                for key, val in user_data['block'].items():
                    print("key", key)
                    block_ids.append(int(key))
                    articles_instance = Articles.objects.get(pk=int(key))
                    article_serializer = ArticleSerializer(articles_instance)
                    article_data[int(key)] = article_serializer.data
                    print("article_data", article_data)
                user_data['blocked_articles'] = article_data
                return Response({'message': 'User fields updated successfully',
                                 'user': user_data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User fields updated successfully, no block',
                                 'user': user_data}, status=status.HTTP_200_OK)
        except:

            return Response({'message':'fail to implement block data'}, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = TestUser
    form_class = CustomUserUpdateForm
    template_name = "users/update_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        try:
            print(self.request.user._wrapped.objects.all())
        except:
            print("cannot self.request.user._wrapped.objects.all()")
        return self.request.user
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


@api_view(['PUT'])
def fake_delete_user(request):
    user = None
    user = token_authentication(request)
    if user is None:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    setattr(user, "deleted_at", timezone.now())
    user.save()
    return Response({'message':f'Successfully deleted user {user.name}'})



@api_view(['POST'])
def logout(request):
    print("logout")
    user = token_authentication(request)

    if user is None:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    user.auth_token.delete()
    user.remember_token = ''
    user.save()
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from allauth.socialaccount.models import SocialToken
import requests
def logoutfromgoogle(request):
    print(f"user is :{request.user}")
    google_token = SocialToken.objects.filter(account__user=request.user, account__provider='google').first()
    print(f"google token is {google_token}")
    if google_token:
        revoke_google_token(google_token.token)

    # Log out from Django
    django_logout(request)

    # Redirect to a logged out page or any other appropriate URL
    return redirect('app-home')

def revoke_google_token(token):
    revoke_endpoint = 'https://oauth2.googleapis.com/revoke'
    data = {'token': token}
    response = requests.post(revoke_endpoint, data=data)

    if response.status_code == 200:
        print('Google token revoked successfully')
    else:
        print('Failed to revoke Google token')

    return response



