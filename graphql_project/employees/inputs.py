import graphene
class EmployeeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    department = graphene.String(required=True)
    salary = graphene.Int(required=True)
