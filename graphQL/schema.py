import graphene
from graphene_django.types import DjangoObjectType
from ingredients import schema


class Query(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
