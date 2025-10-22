#                       <===== first Django app - part 1  =====>

#urls.py --> is url configuration (URLconf) and is mendatory in django app as its used to map the 'view.py' file to a url so that we can access 'view' on browser
    #exp - http://localhost:8000/poll - 

#flow of basic request and response with Django for ur "polls" app  when ran server with "python manage.py runserver"

    # global URLconf (mysite/urls.py) got implemeted then -> local polls's URLconf(polls/urls.py) which included -> views.py path -> httpresponse

#packages and modules =====>

    # "from django.http import HttpResponse" --> use to return httpresponse from view.py

    # "from django.urls import path, include" -->  use it inside urls.py
        # path() -->  expects at least two arguments: route and view
            #exp - path("polls/", include("polls.urls")

        # include() --> The include() function allows referencing other URLconfs.



#                        <===== first Django app - part 2 ======>

#db setup ==> migrations -->
'''
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables 
according to the database settings in your mysite/settings.py file and the database migrations shipped 
with the app (we’ll cover those later).

migrations r derived from ur models file
'''
#creating models ==>

#models = table name of database
#field = attribute(column) of database

'''
models r basically single definitive source of information about ur data.
It contains the essential fields and behaviors of the data you’re storing.
'''
#these classes(models inside of models.py) r nothing but just the table name with variables inside of classs as attribute(columns) of database with their datatype

#activating models ==>
'''
"python manage.py makemigrations polls" to create migrations for those changes
"python manage.py migrate" to apply those changes to the database.

->'makemigration' stores the changes u made in ur models , u can checkout- 
those changes in 'migrations' folder.

"python manage.py sqlmigrate polls 0001" - sqlmigrate command tell u sql command its going to use-
 to create or update models from the code in 'migrations/' folder

"python manage.py check" - checks for any problems in ur project without migrating or touching the db

->'migrate' command takes all the migrations that haven’t been applied and runs them against your database-

->'django_migrations' named table in ur db.sqlite3 tells the 'migrate' command which 'migrations' r applied-
in ur databse already with their publish data. u can check them out in sqlite db

->'migrations' folder also sort of tells all the changes or commits history u did in database

'''

#lol basically the migrate command just makes db tables based on settings(db type) and models(columns of table)
