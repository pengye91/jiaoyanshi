from __future__ import unicode_literals

from django.db import models

from mongoengine import *
from grats_proj.settings import DBNAME

# Create your models here.
connect(DBNAME)


class User(Document):
    email = StringField(required=True, max_length=120)
    first_name = StringField(required=True, max_length=30)
    last_name = StringField(required=True, max_length=30)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {"allow_inheritance": True}


class TextPost(Post):
    content = StringField(required=True)


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()
