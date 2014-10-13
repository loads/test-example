test-example
============

This repository is an example of a load test for Loads.

It contains:

- a **.travis.yml** file that contains all deps for the test to run
- the actual test than needs to be run: **loadtest.py**

Loads will pick up the repo and clone it into a **travis-run** docker 
container, then execute it.
