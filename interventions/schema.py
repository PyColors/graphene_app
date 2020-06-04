import graphene
from graphene_django import DjangoObjectType

from .models import Intervention


class InterventionType(DjangoObjectType):
    class Meta:
        model = Intervention


class Query(graphene.ObjectType):
    interventions = graphene.List(InterventionType)

    def resolve_interventions(self, info, **kwargs):
        return Intervention.objects.all()
