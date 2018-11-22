Docker2metric
=============

This tiny library produces metrics from host's docker containers.

install:

   ``pipenv install --python 3``

run the program : 

   ``pipenv run python main.py # produces metrics as json on stdout``

   ``pipenv run python main.py --send # send one POST request by container to the url specified in .env file for API_URL value``
