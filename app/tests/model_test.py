import unittest
from app.bookstore import store


class store(object):

    def __init__(self, admin, password):
        self.admin = admin
        self.password = password


class books(store):
    def __init__(self, genre, author, price):
        self.genre = genre
        self.author = author
        self.price = price


class library(store):
    def __init__(self, user, category, title, author, genre, edition):
        self.user = user
        self.category = category
        self.title = title
        self.author = author
        self.genre = genre
        self.edition = edition
