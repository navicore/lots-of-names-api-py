Python3 Practice Repo
==========

A practice python env per:

https://medium.com/@greut/building-a-python-package-a-docker-image-using-pipenv-233d8793b6cc

Struggling with best practice for local dev, dockerfile, and pipenv for reliable dev cycles and tools.


This repo starts a python http api server and then calls another api to satisfy the request.


local dev
-----------

```console`
pipenv install
pipenv run python3 ./lots-of-names-api/__init__.py
```
