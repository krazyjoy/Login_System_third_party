""""

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from allauth.socialaccount.adapter import get_account_adapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        if not user.name:
            user.name = user.email


        if not form:
            print("does not have a form")
            email = user.email
            password = email
            form = SignupForm({'email': email, 'password1': password, 'password2': password})
            print("attributes of form: " ,form.__dict__)
            # if not form.cleaned_data.get('password'):


        print("get_account_adapter: save user")
        get_account_adapter().save_user(request, user, form)
        if not EmailAddress.objects.filter(user=user, email=user.email, verified=True):
            print("not email addresses")
            EmailAddress.objects.create(user=user, email=user.email, verified=True, primary=True)
        print("sociallogin.save()")
        sociallogin.save(request)
        print("user", user)
        user.save()
        return user
"""