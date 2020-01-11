from datetime       import datetime
from mongoengine    import Document
from mongoengine    import DateTimeField, StringField


class Bacteria(Document):
    meta = {'collection': 'bacteria'}
    species     = StringField()
    subspecies  = StringField()
    strain      = StringField()
