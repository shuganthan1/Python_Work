from flask import flask
imdb_api =flask(__name__)

@imdb_api.route('/')
def home_page():
    return "I've created my first API service!"

if __name__ ='__main__':
    imdb_api.run()

