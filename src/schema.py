import graphene
from graphene import String
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Microbe as MicrobeModel
from models import Probiotic as ProbioticModel

class Microbe(MongoengineObjectType):
    class Meta:
        model = MicrobeModel
        interfaces = (Node,)
    
    full_name = String()

    @staticmethod
    def resolve_full_name(parent, info):
        return f'{parent.species} {parent.subspecies}'

class Probiotic(MongoengineObjectType):
    class Meta:
        model = ProbioticModel
        interfaces = (Node,)

class AddMicrobe(graphene.Mutation):

    class Input:
        domain      = graphene.String(required=True)
        species     = graphene.String(required=True)
        subspecies  = graphene.String(required=True)
        strain      = graphene.String()

    microbe = graphene.Field(Microbe)

    @staticmethod
    def mutate(root, info, **input):
        bl = MicrobeModel(
            domain      = input['domain'],
            species     = input['species'],
            subspecies  = input['subspecies'],
            strain      = input.get("strain", "Uknown")
        )
        bl.save()
        return AddMicrobe(microbe=bl)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_microbes = MongoengineConnectionField(Microbe)
    all_Probiotics = MongoengineConnectionField(Probiotic)

class Mutation(graphene.ObjectType):

        add_microbe = AddMicrobe.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Microbe, Probiotic])
    