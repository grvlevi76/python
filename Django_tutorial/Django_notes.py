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
