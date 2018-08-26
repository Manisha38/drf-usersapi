# usersapi
## Introduction
A Json based Restful API service for managing user information. Prefixed drf since it is made in Django Rest Framework.
API helps you create, edit, delete users and swap user between bucket.

### Installation
To run it locally you must have the required paackages. Install with:
```pip install -r requirements.txt```

## API Documentation

### Authenticate user
**URL**
http://localhost:8000/user/api/token/

**Description**
Authenticate/login user. Generates a token which is to be used for accessing and modifying user content.

| Endpoint | Method | Description |
|--- | --- | --- |
| user/api/token/ | POST | authenticate user | 


**Parameters**
| Parameter | Description | Parameter type
| --- | --- | --- |
| email | unique value for each user | body |
| password | user password | body |

**Example**
```
curl --request POST \
  --url http://localhost:8000/user/api/token/ \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "user1@abc.com",
    "password": "user123"
}'
```

### Create User
**URL**
```http://localhost:8000/user/create/```

| Endpoint | Method | Description |
|--- | --- | --- |
| user/create/ | POST | Create user |

**Parameters**
| Parameter | Description | Parameter type
| --- | --- | --- |
| token | authentication token | header |
| email | unique value for each user | body |
| password | user password | body |
| first_name | user's first name | body |
| last_name | user's last name | body |
| bucket | bucket number | body |

**Example**
```
curl --request POST \
  --url http://localhost:8000/user/create/ \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "exampe@abc.com",
    "first_name": "example",
    "password": "example123",
    "bucket": 2
}'
```

### Edit user information
** URL **
http://localhost:8000/user/<id>

| Endpoint | Method | Description |
|--- | --- | --- |
| user/<id> | PUT | Update user detail |


**Parameters**
| Parameter | Description | Parameter type
| --- | --- | --- |
| token | authentication token | header |
| email | unique value for each user | body |
| password | user password | body |
| first_name/bucket/last_name | user attribute | body |

**Example** 
```
curl --request PUT \
  --url http://localhost:8000/user/27/ \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "exampe@abc.com",
    "first_name": "example1",
    "password": "example123",
    "bucket": 2
}'
```

### List bucket
** URL **
http://localhost:8000/user/bucket/<bucket_id>

| Endpoint | Method | Description |
|--- | --- | --- |
| user/bucket/<bucket_id> | GET | List of all users in a bucket |

| Parameter | Description | Parameter type
| --- | --- | --- |
| token | authentication token | header |
| bucket_id | bucket number | header |

** Example**
```
curl --request GET \
  --url http://localhost:8000/user/bucket/2 \
  --header 'Content-Type: application/json'
```
  
### Swap user's bucket
**URL**
http://localhost:8000/user/bucket/swap/<id>

| Endpoint | Method | Description |
|--- | --- | --- |
| user/bucket/swap/<id> | PUT | Change user's bucket |

**Parameters**
| Parameter | Description | Parameter type
| --- | --- | --- |
| token | authentication token | header |
| email | unique value for each user | body |
| password | user password | body |
| bucket_id | bucket number | body |

**Example**
```
curl --request PUT \
  --url http://localhost:8000/user/bucket/swap/27 \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "exampe@abc.com",
    "password": "example123",
    "bucket":"5"
}'
```

### Fetch user detail
*** URL ***
http://localhost:8000/user/<id>

| Endpoint | Method | Description |
|--- | --- | --- |
| user/<id> | GET | Fetch details of a user |

**Parameters**
| Parameter | Description | Parameter type
| --- | --- | --- |
| token | authentication token | header |
| id | user is | header |

**Example**
```
curl --request GET \
  --url http://localhost:8000/user/27 \
  --header 'Content-Type: application/json'
```

### Delete user
*** URL ***
http://localhost:8000/user/<id>

| Endpoint | Method | Description |
|--- | --- | --- |
| user/<id> | DELETE | Deletes that particular user |

**Parameters**
| Parameter | Description | Parameter type
| --- | --- | --- |
| token | authentication token | header |
| id | user is | header |

**Example**
```
curl --request DELETE \
  --url http://localhost:8000/user/26 \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "exampe@abc.com",
    "password": "example123",
    "bucket":"5"
}'
```













