import graphene
import employees.schema
import graphql_jwt
class Query(employees.schema.Query, graphene.ObjectType):
    pass
class Mutation(employees.schema.Mutation, graphene.ObjectType):
    # 🔐 JWT Auth Mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)
