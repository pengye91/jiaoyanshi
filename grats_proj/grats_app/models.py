from __future__ import unicode_literals

from django.db import models

from mongoengine import *
from grats_proj.settings import DBNAME

# Create your models here.
connect(DBNAME)


class User(Document):
    email = StringField(required=True, max_length=120)
    first_name = StringField