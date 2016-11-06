# HackYourBrain
An app that uses pictures of food to train your brain to have negative associations with junk food. 
For the We Code Hackathon 2016

# Installation
Install Python 2.7
* clone the project
* cd into the project
```
pip install virtualenv
```
```
virtualenv env
```
On Mac:
```
source env/bin/activate
```
On Windows:
```
source env\Scripts\activate 
# let me know if this works
```
Make sure there is a little (env) in front of your prompt
```
pip install django && pip install pillow
```
```
python manage.py makemigrations trainer && python manage.py migrate
```
```
python manage.py runserver
```
If you get an error like this:
    __import__(name)
ImportError: No module named PIL
Verify  you are running pip version of at least 8.x. Then  run the following:
```
pip install image
```

to create an admin:
```
python manage.py createsuperuser
```
go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and add some models to the database.
Then go to [http://localhost:8000/](http://localhost:8000/)
