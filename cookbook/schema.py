import graphene

import ingredients.schema
import interventions.schema


class Query(ingredients.schema.Query, interventions.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project

    pass


schema = graphene.Schema(query=Query)
