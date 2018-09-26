# HackYourBrain
An app that uses pictures of food to train your brain to have negative associations with junk food. 
For the We Code Hackathon 2016

# Installation
Install Python 3.x
* clone the project
* cd into the project directory
``` bash
cd HackYourBrain
```
* install virtualenv:

``` bash
pip install virtualenv
```
* create a new virtualenv called env
``` bash
virtualenv env
```
* start up your new env

On Mac:
    
``` bash
source env/bin/activate
```
On Windows:

``` bash
source env\Scripts\activate 
```

Make sure there is a little (env) in front of your prompt.
### Install dependencies
This project recently updated for Django 2.1

```
pip install django && pip install pillow
```

### cd to braintrainer directory and run the following: 

```
python manage.py makemigrations trainer && python manage.py migrate
```

```
python manage.py ls
```

If you get an error like this:
``` bash
    __import__(name)
ImportError: No module named PIL
```

Verify you are running pip version of at least 8.x. Then  run the following:
``` bash
pip install image
```

to create an admin:
``` bash
python manage.py createsuperuser
```

### Start the server
``` bash
python manage.py runserver
```

To stop the server, do:

``` bash
CTRL-C
```

To stop virtualenv, type:
``` bash
deactivate
```



# Usage 
Browse to [http://localhost:8000/admin/](http://localhost:8000/admin/) and login 

## First time only
Use the admin page to upload images from your local machine. Also load models.

Then go to [http://localhost:8000/](http://localhost:8000/)
