# Django-rest framework
========================================================
## How to run the Project
- Install Postgreql
- Install Python
- Git clone the project with ``` git clone git@github.com:No-Country/c7-15-m-python.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with 
```sh
$pip install -r requirements.txt
```
- Create you database with
```sh
$python manage.py runserver
```
- Finally run the API 
```sh
$python manage.py runserver
```
========================================================

## KECOMER - BACK END API


## ROUTES TO IMPLEMENT
| METHOD | ROUTE                        | FUNCTIONALITY                    |ACCESS|
|--------|------------------------------|----------------------------------| ------------- |
| *POST* | ```/users/signup/```         | _Register new user_              | _All users_|
| *POST* | ```/auth/jwt/create/```      | _Login user_                     |_All users_|
| *POST* | ```/auth/jwt/refresh/```     | _Refresh the access token_       |_All users_|
| *POST* | ```/auth/jwt/verify/```      | _Verify the validity of a token_ |_All users_|
| *GET*  | ```/users/update/{id}/```    | _Retrieve an user_               |_All users_|
| *PUT*  | ```/users/update/{id}/```    | _Update an user_                 |_All users_|
| *GET*  | ```/recipes/recipes/``` | _List all recipe_                |_All users_|

