import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Microbe as MicrobeModel
from models import Probiotic as ProbioticModel

class Microbe(MongoengineObjectType):
    class Meta:
        model = MicrobeModel
        interfaces = (Node,)

class Probiotic(MongoengineObjectType):
    class Meta:
        model = ProbioticModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_microbes = MongoengineConnectionField(Microbe)
    all_Probiotics = MongoengineConnectionField(Probiotic)

schema = graphene.Schema(query=Query, types=[Microbe, Probiotic])
    