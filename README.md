Docker2metric
=============

This tiny library produces metrics from host's docker containers.

install:

   ``pip install docker2metric``

run the program : 

   ``python -m docker2metric # produces metrics as json on stdout``

   ``python -m docker2metric --send # send one POST request by container to the url specified in .env file for API_URL value``
