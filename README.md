# AllAuth-Routes

`127.0.0.1:8000/`

navbar: 
- authenticated
	![](images/index_navbar.png)
	- Home: `home/` $\rightarrow$ `templates/dashboard/home.html`
	- Change E-Mail 
    - Sign out : (route) `accounts/logout` $\rightarrow$ (templates) `templates/account/logout.html`
    ![](images/sign_out.png)
- unauthenticated
	
	![](images/navbar2.png)

  - Sign In : `accounts/login/` $\rightarrow$ `templates/account/login.html` 
	  
       ![](images/sign-in-page.png)

  - sign-in with google: `accounts/google/login/?process=login` (default template)
     $\rightarrow$ `Continue` button 
			
     ![](images/sign-in-via-google 1.png)
     $\rightarrow$ google sign in prompt
     ![](images/google-oauth-signin-prompt.png)
  - Sign Up : (required before using google sign-in)

	
- Regular Sign-In


`username`: `chihyi`
`password`: `<same as my-gmail-account>`

- redirects back to `/home`
![](images/regular-sign-in-redirect.png)



# AllAuth Templates


Retrieve records using python shell
1. runserver in one terminal
2. activate virtual environment and enter python shell
```
python manage.py shell (e.g. :/mnt/c/Users/huang/OneDrive/桌面/OIN/login_app/version2/django_project)


from users.models import TestUser

records = TestUser.objects.all()

for record in records:
	print(record.__dict__) # check accessible attributes and their values
```



## Project Urls

`/`: `/users/templates/users/account_base.html`

`/home`: `/templates/dashboard/home.html`

`api/`: `regular CRUD` (app level)
- `api/register`
- `api/login`
- `api/update`
- `api/delete`
- `api/logout`

`accounts/`: `allauth` (project level)
- `accounts/logout`
- `accounts/login`
- `accounts/signup`


```
# root_app/urls
urlpatterns = [  
	path('admin/', admin.site.urls),  
	path('api/', include('users.urls')),  
	path('accounts/', include('allauth.urls')),  
	path('', TemplateView.as_view(template_name='users/account_base.html'), name='app-home'),  
	path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),  
]
```


```
# users/urls
urlpatterns = [  
	path('register/', register_user, name = 'register'),  
	path('login/', user_login, name = 'login'),  
	path('update/', update_user, name='update'),  
	path('delete/', fake_delete_user, name='delete'),  
	  
]
```


## login template

```
{% extends "users/account_base.html" %}  
  
{% load i18n %}  
{% load account socialaccount %}  
  
{% load crispy_forms_filters %}  
  
  
{% block content %}  
```

```
<div class="text-center mt-3">  
	<h1>{% trans "Sign In" %}</h1>  
```

- there are `socialaccount_providers`
	- `include the provider_list.html`
	- `reauthenticate`
	- include `socialaccount/snippets/login_extra.html`
```
	{% get_providers as socialaccount_providers %}  
  
		{% if socialaccount_providers %}  
			<p>{% blocktrans with site.name as site_name %}Please sign in with one  
			of your existing third party accounts.  
			<br>  
			Or, <a href="{{ signup_url }}">sign up</a>  
			for a {{ site_name }} account and sign in below:{% endblocktrans %}  
			</p>  
  
			<div class="socialaccount_ballot">  
  
				<div class="socialaccount_providers">  
				{% include "socialaccount/snippets/provider_list.html" with process="login" action="reauthenticate"%}  
				</div>  
  
				<div class="login-or border-top border-bottom my-3">
					{% trans 'OR' %}
				</div>  
				  
			</div>  
```

- there aren't `socialaccount_providers`
	-recommend to do a regular sign-up `signup_url`

```
{% include "socialaccount/snippets/login_extra.html" %}  
  
{% else %}  
	<p>{% blocktrans %}If you have not created an account yet, then please  
		<a href="{{ signup_url }}">sign up</a> first.{% endblocktrans %}
	</p>  
{% endif %}  
</div>  
```

- sign-in form
	- action: `url 'account_login'`
	- `redirect_field_name`: `csrfmiddlewaretoken`
	- `redirect_field_value`: `JSXTG8Ivsqw5RL9TaJ5wq2sJda0j2Ax5JolyBfENwWV4zkjunyx7UyNzZF1uGg86`
![](images/sigin-template.png)



```
	
<div class="row">  
	<div class="col-md-6 offset-md-3">  
		<form class="login" method="POST" action="{% url 'account_login' %}">  
			{% csrf_token %}  
			{{ form|crispy }}  
			{% if redirect_field_value %}  
				<input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />  
			{% endif %}  
			<div class="d-grid">  
				<button class="primaryAction mt-3 btn btn-dark" type="submit">
				{% trans "Sign In" %}
				</button>
				<br>  
				<a class="button secondaryAction text-dark text-center" href="{% url 'account_reset_password' %}">
					{% trans "Forgot Password?" %}
				</a>  
			</div>  
		</form>  
	</div>  
</div>  
{% endblock %}
```


## Update profile

http://127.0.0.1:8000/accounts/login/?next=/api/update_profile/

redirect to accounts/login before updating_profile

`settings.py`

`LOGIN_URL='/accounts/login'`


```
  
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
```



`users/forms.py`

```
class CustomUserUpdateForm(forms.ModelForm):  
	avatar = forms.CharField(max_length=200, required=False)  
	gender = forms.CharField(max_length=10, required=False)  
	birthday = forms.DateTimeField(required=False)  
	phone = forms.CharField(max_length=256, required=False)  
	website = forms.CharField(max_length=100, required=False)  
	biography = forms.CharField(widget=forms.Textarea, required=False)  
	zipcode = forms.CharField(max_length=10, required=False)  
	country = forms.CharField(max_length=50, required=False)  
	state = forms.CharField(max_length=100, required=False)  
	city = forms.CharField(max_length=120, required=False)  
	address = forms.CharField(max_length=512, required=False)  
	block = forms.JSONField(required=False)  
	article = forms.JSONField(required=False)  
	class Meta:  
		model = TestUser  
		fields = ("name",  
		"avatar", 'gender', 'birthday', 'phone', 'website',  
		'biography', 'zipcode', 'country', 'state', 'city', 'address',  
		'block', 'article')  
	  
	def __init__(self, *args, **kwargs):  
		super().__init__(*args, **kwargs)  
	  
  
	def save(self, commit=True):  
		user = super().save(commit=False)  
		user.name = self.cleaned_data['name']  
		user.avatar = self.cleaned_data['avatar']  
		user.gender = self.cleaned_data['gender']  
		user.birthday = self.cleaned_data['birthday']  
		user.phone = self.cleaned_data['phone']  
		user.website = self.cleaned_data['website']  
		user.biography = self.cleaned_data['biography']  
		user.zipcode = self.cleaned_data['zipcode']  
		user.country = self.cleaned_data['country']  
		user.state = self.cleaned_data['state']  
		user.city = self.cleaned_data['city']  
		user.address = self.cleaned_data['address']  
		user.block = self.cleaned_data['block']  
		user.article = self.cleaned_data['article']  
		user.is_active = True  
		if commit:  
			user.save()  
	  
	return user
```



# Prone to Errors

## Integrity Error

when using third party authentication, it does not fill out the attributes on the model
(same error occurred, when I tried to use regular register method)

 
-  solution:  add `blank=True` prior to `null=True`, `default=None`
	- `null=True`, `default=None` is still needed when doing `python manage.py migrate`
	```
	It is impossible to change a nullable field 'deleted_at' on testuser to non-nullable without providing a default. This is because the database needs something to populate existing rows.
	Please select a fix:
	 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
	 2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
	 3) Quit and manually define a default value in models.py.
	```

	`website = models.CharField(max_length=100, null=True, default=None)`
	
	$\rightarrow$
	`website = models.CharField(max_length=100, blank=True, null=True, default=None)`


## Unable to Signout

![](images/unable_to_signout.png)


Cannot find the corresponding user to sign out from


## Unable to see fields email from Google OAuth2

Certainly! It seems you’re facing an issue with obtaining email addresses while using **Django Allauth**. Let’s troubleshoot this together.

To ensure that email addresses are retrieved successfully, consider the following steps:

1. **Check Scopes**:
    - In your `settings.py`, make sure you’ve set the correct scopes for Google authentication. [Specifically, the **SCOPE** should include both `'profile'` and `'email'`](http://django-allauth.readthedocs.org/en/latest/providers.html)[1](http://django-allauth.readthedocs.org/en/latest/providers.html).
    - Here’s an example of how it should look:
        
        ```python
        SOCIALACCOUNT_PROVIDERS = {
            'google': {
                'SCOPE': ['profile', 'email'],
                'AUTH_PARAMS': {'access_type': 'online'}
            }
        }
        ```
        
2. **Verify Other Settings**:
    - Ensure that other relevant settings are correctly configured. For instance:
        - `ACCOUNT_EMAIL_REQUIRED` should be set to `True`.
        - `SOCIALACCOUNT_QUERY_EMAIL` should be `True`.
    - [You can also explore additional settings related to email verification and authentication methods](https://stackoverflow.com/questions/23956288/django-all-auth-email-required)[2](https://stackoverflow.com/questions/23956288/django-all-auth-email-required)[3](https://www.codesnail.com/django-allauth-email-authentication-tutorial/).
3. **Debugging**:
    - If the issue persists, consider debugging by:
        - Checking logs for any error messages.
        - Verifying that the Google API credentials are correctly set up.
        - Testing with a minimal reproducible example to isolate the problem.

Remember that email retrieval is essential for user authentication and communication. If you encounter further difficulties, feel free to ask for more assistance! 🌟


- tables saved:
	- users_testuser
	- account_emailaddress
	- socialaccount_socialaccount




## Weird Password saved to Users model

[customUserAuthentication/customUser at main · Nathius262/customUserAuthentication (github.com)](https://github.com/Nathius262/customUserAuthentication/tree/main/customUser)



## Unable to signup a new user through social authentication without regular signup

- weird password saved to table `users_testuser`
- no way to retrieve third party sign-in password

solution:
regular signup $\rightarrow$ connect to third party


# Workflow
## Intercept Social Auth Process Information Through Signal 

1. register for signal in `users.apps.py`
	```
	from django.apps import AppConfig  
	class UsersConfig(AppConfig):  
	default_auto_field = 'django.db.models.BigAutoField'  
	name = 'users'  
	def ready(self):  
		import users.signals	
	```

```
# users.signals.py

from allauth.socialaccount.signals import pre_social_login, social_account_added  
from django.dispatch import receiver
```

2. `pre_social_login_callback()`
	- `sociallogin`  parameter
		- `social_account`
		- `social_account.provider`
		- `social_account.uid`
		- `social_account.extra_data`
	
```
inside: `users.signals.py`


@receiver(pre_social_login)  
def pre_social_login_callback(sender, request, sociallogin, **kwargs):  
  

	social_account = sociallogin.account  
	# Inspect the data received from the OAuth2 provider  
	try:  
  
		print("Provider: ", social_account.provider)  
		print("User ID: ", social_account.uid)  
		print("Extra Data: ", social_account.extra_data)  
	except:  
		print("unable to print keys")

```
	e.g. `chihyi2323@gmail.com` connection

![](images/pre_social_login.png)

3. `social_account_added_callback()`
	- signal: `social_account_added`
	- `socaillogin` parameter
		- `social_account`
		- `sociallogin.user`
		- `sociallogin.email_addresses` # need the google `SCOPE` and `AUTH_PARAMS` setup

`settings.py`
```
SOCIALACCOUNT_PROVIDERS = {  
	'google': {  
		'APP': {  
		'client_id': '212242759090-n4rmcl4taj63cmoebd3tdh4of2tvjido.apps.googleusercontent.com',  
		'secret': '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',  
		'key': ''  
		},  
	'SCOPE':[  
		'profile',  
		'email'  
	],  
	'AUTH_PARAMS': {'access_type': 'online'}  
	}  
}
```

![](images/social_account_added.png)
4. `social_account_updated_callback()`
	- signal: `social_account_updated`
	- same as `social_account_added_callback`
![](images/social_account_updated.png)



## Reauthenticate

- issue: after 1 registration with google oauth2 under same ip, when click the google sign-in button, it directly signs in to the previous account, but reauthentication and add new google account is preferred

`settings.py`

```
SOCIALACCOUNT_PROVIDERS = {  
	'google': {  
		'APP': {  
			'client_id': '212242759090-n4rmcl4taj63cmoebd3tdh4of2tvjido.apps.googleusercontent.com',  
			'secret': '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',  
			'key': ''  
		},  
		'SCOPE':[  
			'profile',  
			'email'  
		],  
		'AUTH_PARAMS': {  
			'access_type': 'online',  
			'prompt': 'login',  # this is added to reauthenticate
		}  
	}  
}
```


## Connections

`accounts/social/connections/`


![](images/account_connections.png)



`pip install allauth allows form.accounts` to be accessible

1. create a list of provider to account connections 
	-  for loop over `form.accounts`
		- `base_account.id`
		- `base_account.get_provider_account as account`
			- `account.get_brand_name`
			- `account`

- original using arrows
```
{% if form.accounts %} # has social account

	<form method="post" action="{% url 'socialaccount_connections' %}">
		{% csrf_token %}
	
		<fieldset>
		{% if form.non_field_errors %} # has field error
			<div id="errorMsg">
				{{form.non_field_errors}}
			</div>
		{% endif %}
	{% for base_account in form.accounts %}
		{% with base_account.get_provider_account as account %}
			<div>
			<label for='id_account_{{base_account.id}}' >
			<input id='id_account_{{base_account.id}}'
				type = "radio"
				name = "account"
				value = "{{base_account.id}}"/>
			<span>
				{{account.get_brand_name}}
				-> {{account}}
			</span>
			</div>
		{% endwith %}
	{% endfor %}	
	

```

- after: using table representation
	
| provider | account  | select    |
| -------- | -------- | --------- |
| Google   | username | check-box |

### Styling table

- center content
```
<div class="container mx-auto">  
<div class="text-center">  


```
- center table (add class)
	- `mx-auto`
- add border (with paddings)
	- `<table class=table-bordered>`
		- `<th class="p-3">`
		- `<td class="p-3">`

```
{% extends "users/account_base.html" %}  
{% load static %}  
{% load i18n %}  
{% load allauth %}  
{% block head_title %}{% trans "Account Connections" %}{% endblock %}  
```


### connection table

- use form to wrap a table, and send `remove` submission if checkbox account is ticked
which directs to `socialaccount_connections`
- use `form.accounts` to access `connection` records

```  
<form method="post" action="{% url 'socialaccount_connections' %}">
	<!-- base account information: provider -> 3rd_party_account -->  
	<table class="connection_table mx-auto table-bordered p">  
		<thead>  
			<tr>  
				<th class="p-3">Provider</th>  
				<th class="p-3">Account</th>  
				<th class="p-3">Select</th>  
			</tr>  
		</thead>  
		<tbody>  
			{% for base_account in form.accounts %}  
			{% with base_account.get_provider_account as account %}  
				<tr>  
					<td class="p-3">  
						<span class="socialaccount_provider {{ base_account.provider }} {{ account.get_brand.id }}">  
						{{account.get_brand.name}}  
						</span>  
					</td>  
					<td class="p-3">  
						{{account}}  
					</td>  
					<td class="p-3">  
						<input id="id_account_{{ base_account.id}}" type="checkbox" name="accounts" value="{{base_account.id}}">  
						<label for="id_account_{{ base_account.id }}"></label>  
					</td>  
				</tr>  
			{% endwith %}  
			{% endfor %}  
		</tbody>  
	</table>  
	  
	<!--remove social account from user -->  
	<div class="my-4">  
		<button class="btn btn-dark" type="submit">{% trans 'Remove' %}</button>  
	</div>  
	  
	</fieldset>  
  
</form>  

```

![](images/connection_table.png )

- issue: the checkbox/radio button inside the table does not remove the connection


# Django Restful Framework
## Sign Up User

`users/views.py`
- checks if username is used before
- takes the `UserSerializer` object and send back data after creation

```
@api_view(['POST'])  
def register_user(request):  
	if request.method == 'POST':  
		serializer = UserSerializer(data=request.data)  
	if serializer.is_valid():  
		serializer.save()  # save to db
		return Response(serializer.data, status = status.HTTP_201_CREATED)  
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

`users/urls.py`
```
  
urlpatterns = [  
	path('register/', register_user, name = 'register')
]
```


## Update User


### Return user object for each restful API

- `serializers.serializer('json', [object, ])`
```
from rest_framework import status  
from rest_framework.response import Response  
from rest_framework.decorators import api_view



from django.core import serializers

@api_view(['PUT'])
def api_call(request):
	user_data = serializers.serialize('json', [users, ])
	
	return Response({'message': '<correct_message>', 'users': user_data}, 
	status = status.HTTP_200_OK)


```


- `serializer.data`

```
{

    "message": "User fields updated successfully",

    "user": "{\"name\": \"v2user\", \"email\": \"v2user@gmail.com\", \"register_from\": \"default\", \"avatar\": \"hihi v2 user profile say hi to me\", \"gender\": \"male\", \"birthday\": \"1989-07-19T00:00:00Z\", \"phone\": \"5403857340870\", \"website\": \"linkedin-v2user\", \"biography\": \"this is v2user welcome to my home page\", \"state\": \"MA\", \"city\": \"Boston\", \"address\": \"John F. Kennedy Presidential Library, Columbia Point, Boston, MA 02125\", \"country\": \"United States\", \"zipcode\": \"02125\"}"

}
```

### Make block articles visible 

- import block_articles with ArticleSerializer
- add 'block' in UserSerializer in both create and Meta field
```
  
class UserSerializer(serializers.ModelSerializer):  
	blocked_articles = ArticleSerializer(many=True, read_only=True, source='get_blocked_articles')  
	  
	class Meta:  
		model = TestUser  
		  
		fields = ['name', ...  
		'block', 'blocked_articles']  
		extra_kwargs = {'password':{'write_only': True}}  
		  
def create(self, validated_data):  
	user = TestUser(  
		name = validated_data['name'],  
		... 
		block = validated_data['block']  
	)  
	  
	user.set_password(validated_data['password'])  
	user.save()  
	return user
```


- update 時, token取得使用者資訊
```
from rest_framework.authtoken.models import Token


token_key = request.headers.get('Authorization').split(' ')[1]

token = Token.objects.get(key = token_key)

user = token.user
```

- serializer 組成 dictionary
```
user_serializer = UserSerializer(user)
user_data = user_serializer.data

```

- Django query by id
```
article_instance = Articles.objects.get(pk=int(key))
```

- instance 放進serializer，轉換成 article_serializer
```
article_serializer = ArticleSerializer(article_instance)
article_data[int(key)] = article_serializer.data
```


## User Serializer
- purpose: to serialize object to present to frontend API
```
django_project <root project>
|
|--------<apps>
|
|--------users
|
|--------articles
|
|--------django_project app
```

## CREATE Articles APP

```
from rest_framework import serializers  
from .models import TestUser  
from articles.serializer import ArticleSerializer  
  
class UserSerializer(serializers.ModelSerializer):  
blocked_articles = ArticleSerializer(many=True, read_only=True, source='get_blocked_articles')  
  
class Meta:  
model = TestUser  
  
fields = ['name', 'email', 'password', 'register_from', 'avatar',  
'gender', 'birthday', 'phone', 'website', 'biography',  
'state', 'city', 'address', 'country', 'zipcode',  
'block', 'blocked_articles']  
extra_kwargs = {'password':{'write_only': True}}  
  
def create(self, validated_data):  
user = TestUser(  
name = validated_data['name'],  
email = validated_data['email'],  
register_from = validated_data['register_from'],  
avatar = validated_data['avatar'],  
gender = validated_data['gender'],  
birthday = validated_data['birthday'],  
phone = validated_data['phone'],  
website = validated_data['website'],  
biography = validated_data['biography'],  
zipcode = validated_data['zipcode'],  
country = validated_data['country'],  
state = validated_data['state'],  
city = validated_data['city'],  
address = validated_data['address'],  
block = validated_data['block']  
)  
  
user.set_password(validated_data['password'])  
user.save()  
return user
```



```
CREATE TABLE articles (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid BINARY(16) DEFAULT (UUID()),
    api_feed_id BIGINT UNSIGNED,
    source_name TEXT,
    source_uuid TEXT,
    title TEXT,
    description TEXT,
    context TEXT,
    source_url TEXT,
    image_url TEXT,
    author VARCHAR(200),
    published_at VARCHAR(200),
    symbols VARCHAR(200),
    sectors VARCHAR(200),
    industries VARCHAR(200),
    report VARCHAR(20),
    created_at VARCHAR(200),
    update_at VARCHAR(200),
    deleted_at VARCHAR(200)
);


```

- install pymysql
	- use connection string to connect to mariadb
```
def insert_csv_to_pymysql(filepath, table):
    df = pd.read_csv(filepath)
    df.to_sql(table, con=engine, if_exists='replace')
    sql_query = f'SELECT * FROM {table} data LIMIT 5'
    df2 = pd.read_sql_query(sql_query, engine)
    print(df2.head())
    

def connect_to_pymysql():
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'user1'
    database = 'testsite'
    
    engine = create_engine(
        'mysql+pymysql://root:user1@localhost:3306/testsite'
    )
    
    return engine
    

if __name__ == "__main__":
    
    connect_to_pymysql()
    insert_csv_to_pymysql("articles.csv", "articles")
    
```


- generate models.py from existed table
	- table: articles
	```
	python manage.py inspectdb articles > models.py
	```

- add block article data to a user 

```
144.24.33.22/api/update

{

    "block":{

        "3":"cf0164bd-e19c-4b71-9303-65ca860f1e4b"

    }

}
```


![](images/add_block_data.png)


## Delete User

`users/views.py`
`api/delete`
- use token to verify user identification
-  `deleted_at` field add the datetime when deletion is called

```
@api_view(['PUT'])  
def fake_delete_user(request):  
	user = None  
	user = token_authentication(request)  
	if user is None:  
	return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)  
	  
	setattr(user, "deleted_at", timezone.now())  
	user.save()  
	return Response({'message':f'Successfully deleted user {user.name}'})
```

`users/urls.py`

```
urlpatterns = [
	path('delete/', fake_delete_user, name='delete'),
]
```