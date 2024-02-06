# Django notes

Changing the plural of a class name:

````
// ```python
class Meta:
       verbose_name_plural = "statuses"
```
````

Implement Token Authentication using DRF (viewsets) :

class: serializers.py

```

from rest_framework import serializers
from django.contrib.auth.models import User


class userSerializers(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'

```

class: viewsets.py

```

from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth.models import User


class userviewsets(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = userSerializers

```

class: settings.py

```

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
               'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
                'rest_framework.permissions.IsAuthenticated',
    ),

}
```

class: router.py

```
from user.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', userviewsets, base_name ='user_api')

```

class: urls.py

```
from .router import router
from rest_framework.authtoken import views

path('api/', include(router.urls)),
path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

```



Testing API

```
http POST http://localhost:8000/api-token-auth/ username='your_username' password="your_password"

http http://localhost:8000/api/user/ "Authorization: Token API_KEY_HERE"
```

\
Q query:

```
from django.db.models import Q
```

```python
query=Q(pk__isnull=False,active=True,processed=processed
query &= Q(page__in=filter.filters['page_id'])
query &= ~Q(page__in=filter.filters['page_id'])  query whit NOT

```

