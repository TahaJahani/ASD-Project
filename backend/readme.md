# Trello Backend Project
### How to run project
First ensure that python 3.10 is properly installed on your device. Then run these commands to configure project:
```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r pip-requirements.txt
```
To run the project, first ensure that docker and docker-compose are installed on your system. Then run these commands:
```shell
$ sudo docker-compose up -d
$ sudo docker exec -it backend_postgres_1 bash
$ psql -U postgres
$ create database db
$cockAndBallTorture
```
Then exit from the shell and inside a new terminal, execute following commands to run the migrations:
```shell
$ python3 manage.py migrations
$ python3 manage.py runserver
```
Open `http://localghost:8000/auth/test` to see if the server is working.
