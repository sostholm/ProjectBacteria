from datetime       import datetime
from mongoengine    import Document
from mongoengine    import (
    DateTimeField, StringField, ReferenceField, ListField
)


class Microbe(Document):
    meta        = {'collection': 'microbes'}
    m_type      = StringField()
    species     = StringField()
    subspecies  = StringField()
    strain      = StringField()


class Probiotic(Document):
    meta = {'collection': 'probiotic'}
    name = StringField()
    microbes = ListField(ReferenceField(Microbe))