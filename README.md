# tuzimbe
Tuzimbe is a construction site app for people to keep track of workers and building material at their construction sites.

### Requirements
`Python 3+, python-pip, virtualenv`

### Create a virtualenv, and activate it:
Install and start your virtualenv
https://virtualenv.pypa.io/en/latest/installation.html

application

### Then install all dependecies required to run the application

```
pip install requirements.txt
```
### Create thge database :
copy contents of .env.example to .env
add details of the database to .env
### Then, run the application:
```
$ python run.py
```
### To see the application running:
Install postman and access the application at:

```
http://localhost:5000
```


## API Resources
| HTTP METHOD | ENDPOINT | DESCRIPTION |
|:-----------:| :---: | :---: |
|    POST     | /api/v1/register | register a user{name:"", user_type:""}
|    POST     | /api/v1/work/daily | add worker details{name:"james", arrival_time:"2022-10-10 10:10:00", departure_time:"2022-10-10 10:10:00", daily_rate:20}
|    POST     | /api/V1/materials/usage| add material details{material_type:"sand", quantity:"300", unit_price:"1000000"}
|    GET     | /api/v1/materials/usage| get material details{name:"james"}


### Testing
The application tests are based on python's unit testing framework unittest. to run the test with nose

> nosetests tests
