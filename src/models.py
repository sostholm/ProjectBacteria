from datetime       import datetime
from mongoengine    import Document
from mongoengine    import (
    DateTimeField, StringField, ReferenceField, ListField
)

MICROBE_TYPES = ['Archaea', 'Bacteria', 'Fungi', 'Protists']

class Microbe(Document):
    meta        = {'collection': 'microbes'}
    domain      = StringField(choices=MICROBE_TYPES)
    species     = StringField(required=True)
    subspecies  = StringField(required=True)
    strain      = StringField(unique_with=['species', 'subspecies'], default='Unknown')


class Probiotic(Document):
    meta = {'collection': 'probiotic'}
    name = StringField(required=True, unique=True)
    microbes = ListField(ReferenceField(Microbe))

