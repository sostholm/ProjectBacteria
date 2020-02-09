import graphene
from graphene import String
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Microbe as MicrobeModel
from models import Probiotic as ProbioticModel

import json
import sys
from graphql.utils import schema_printer

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

class AddProbiotic(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    probiotic = graphene.Field(Probiotic)

    @staticmethod
    def mutate(root, info, name):
        pb = ProbioticModel(name=name)
        pb.save()
        return AddProbiotic(probiotic=pb)

class UpdateProbiotic(graphene.Mutation):
    class Arguments:
        _id = graphene.String()
        microbe_ids = graphene.List(graphene.String)

    probiotic = graphene.Field(Probiotic)

    @staticmethod
    def mutate(root, info, _id, microbe_ids):
        pb = ProbioticModel.objects(id=_id).first()
        for m_id in microbe_ids:
            pb.microbes.append(MicrobeModel.objects(id=m_id).first())
        pb.save()
        return AddProbiotic(probiotic=pb)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_microbes = MongoengineConnectionField(Microbe)
    all_Probiotics = MongoengineConnectionField(Probiotic)

class Mutation(graphene.ObjectType):
        add_microbe = AddMicrobe.Field()
        add_probiotic = AddProbiotic.Field()
        update_probiotic = AddProbiotic.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Microbe, Probiotic])
    
def print_schema():
    my_schema_str = schema_printer.print_schema(schema)
    fp = open("schema.graphql", "w")
    fp.write(my_schema_str)
    fp.close()