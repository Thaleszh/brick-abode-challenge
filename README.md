# Brick Abode Challenge

The challenge was done by Thales A. Zirbel Hubner using the language 
Python and the Django REST framework.

## Prerequisites

- [Python 3.8](https://www.python.org)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- Git

## Instructions to Run

- Clone this repository and move to it

        git clone https://github.com/Thaleszh/brick-abode-challenge/
        cd brick-abode-challenge
- Create a python virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Create DB and make migrations `python manage.py migrate`
- Load sample data into the db `python manage.py loaddata trades/fixtures/initial_data.json`
- Run a sample query script `python manage.py shell < small_queries.py`

## DB Modelling and Usage
For this work I've used SQLite for database and used schema and migrations offered with Django.
The database can be switched with only a handful of setting changes and requisites. 
The data can also be moved via intermediate json.

The following tables and fields were made into the database. 
There are a few validations being enforced by the schema.
Each one also has an unique id as a primary key.

- **Provider** - Source of prices.
    - <ins>name</ins> - An unique string of up to 64 characters.
- **Pair** - A monetary pair provided with a price at a given time.
    - <ins>name</ins> - A currency pair. I could have enforced a regex to enforce a `3-letter / 3-letter` pattern but didn't know 
    enough to apply it
    - <ins>time</ins> - A DateTime field, by default the current time.
    - <ins>price</ins> - A positive float value, defining the stock price.
    - <ins>provider</ins> - A foreign key for a provider.
- **Deal** - A quantity of pairs' stock bought.
    - <ins>quantity</ins> - An unsigned integer.
    - <ins>pair</ins> - A foreign key to a pair.

## Json API
Django allows usage of Json API with a combination of a serializer, a viewset and an url.
The serializer transforms the db data to a json, the viewset dictates the REST interface and the url the endpoint access.

The endpoints data access with a few URLs in a webpage. You can access them with:
- Launch the server with `python manage.py runserver`
- Check a json from db with the following URLs:
    - Provider: http://127.0.0.1:8000/providers/
    - Pair: http://127.0.0.1:8000/pair/
    - Deal: http://127.0.0.1:8000/deal/
- You can access a specific point by adding an id after the link. For example: http://127.0.0.1:8000/pair/1/
- The basic REST interactions are supported.

## Admin Interface
Django also comes with a default admin interface to interact with the DB.
To use it, follow these steps:
- Create a superuser `python manage.py createsuperuser`
- Launch a server with endpoints with `python manage.py runserver`
- Login with the superuser into the webpage on  http://127.0.0.1:8000/admin
