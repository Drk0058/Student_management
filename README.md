# Student_management

A college management system built using Django framework. It is designed for interactions between students and teachers. Features include attendance, marks and time table,classwide chatroom and notfications from institute.

## Installation

Python,Django,Django-channells and Redis need to be installed

```bash
pip install django
pip install redis
pip install django-channels
```

## Usage

Go to the Student Management folder and run

```bash
cd req/Redis
redis-server
cd ..
cd ..
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for students and teachers.
The username is their name and password for everyone is 'boomshakalaka'.
Example usernames:

student- 'Divinesh'

teacher- 'GKVerma'

You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username 'drk' and the password- "password".

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Alerts,Students, Teachers, Departments, Courses, Classes etc.

## Screenshots

### Teacher Page

![alt text](https://imgur.com/TBZsgf2.png)

![alt text](https://i.imgur.com/x53ejWU.jpg?1)

![alt text](https://i.imgur.com/sVa2nDm.jpg?1)

![alt text](https://i.imgur.com/bynQV8f.jpg?1)

![alt text](https://i.imgur.com/ssuzaW4.jpg?1)

![alt text](https://i.imgur.com/NCEQ3Bf.jpg?1)

![alt text](https://i.imgur.com/vUenp2y.jpg?1)

### Student Page

![alt text](https://i.imgur.com/H8pMxNC.jpg?1)

![alt text](https://i.imgur.com/ZMunvIf.jpg?1)

![alt text](https://i.imgur.com/IF4k3gf.jpg?1)

![alt text](https://i.imgur.com/Ba5geg1.jpg?1)

![alt text](https://i.imgur.com/TnDBgGw.jpg)

![alt text](https://i.imgur.com/OyPFtx9.jpg?1)

![alt text](https://i.imgur.com/kXT3cWQ.jpg?1)

### Admin Page

![alt text](https://i.imgur.com/JDYmdlr.jpg?1)

![alt text](https://i.imgur.com/lX3STKE.jpg?1)
