test-example
============

This repository is an example of a load test for Loads.

It contains a **Dockerfile** file that contains all the configuration needed to 
build a container for the test.

the actual test than needs to be run is launched via a CMD command in the
docker file, and in our case the tets is in **loadtest.py**.

Loads will pick up the repo and build the docker container, then use it
to run tests.

We're providing here examples on how to produce results to send via Heka, 
which will send it to the Loads InfluxDB database.
