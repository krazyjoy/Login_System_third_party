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

```

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

144.24.33.22/api/update

{

    "block":{

        "3":"cf0164bd-e19c-4b71-9303-65ca860f1e4b"

    }

}
```


![[add_block_data.png | 500]]


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