# Fastapi Practice
Basic CRUD with authentication by oauth2

## Basic install setup:
1. Use pip3 install -r requirements.txt to intall all packges
2. use "uvicorn main:app --reload" to turn on the local server

## Description
### Blog API (Version 1)
This project simple create few endpoints to create and delete posts without login.
And upload image to selected local folder.

### Blog API (Version 2)
Similar with version 1
But user can create and login to their account and use jwt token to access protected endpoints.
And add new comment to posts.
They can also upload image to selected local folder.
