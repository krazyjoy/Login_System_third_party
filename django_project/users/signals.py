from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import pre_social_login, social_account_added
from django.dispatch import receiver

# Define a receiver function to intercept the social login process
@receiver(pre_social_login)
def pre_social_login_callback(sender, request, sociallogin, **kwargs):

    # Access the SocialAccount object associated with the login
    social_account = sociallogin.account
    # Inspect the data received from the OAuth2 provider
    try:

        print("Provider: ", social_account.provider)
        print("User ID: ", social_account.uid)
        print("Extra Data: ", social_account.extra_data)
    except:
        print("unable to print keys")

@receiver(social_account_added)
def social_account_added_callback(sender, request, sociallogin, **kwargs):
    social_account = sociallogin.account
    user = sociallogin.user
    email = sociallogin.email_addresses
    print("Social account added for user:", user.username)
    print("Social emails: ", email)
    print("Provider:", social_account.provider)
    print("Extra data:", social_account.extra_data)

@receiver(social_account_added)
def social_account_updated_callback(sender, request, sociallogin, **kwargs):
    social_account = sociallogin.account
    user = sociallogin.user
    email = sociallogin.email_addresses
    print("Social account updated for user:", user.username)
    print("Social emails: ", email)
    print("Provider:", social_account.provider)
    print("Extra data:", social_account.extra_data)