import graphene
from graphene_django import DjangoObjectType
from .models import Employee
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from .filters import EmployeeFilter
from graphene_django.filter import DjangoFilterConnectionField
class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node,)
        fields = "__all__"
class Query(graphene.ObjectType):
    # 🔹 Basic Queries
    all_employees = DjangoFilterConnectionField(EmployeeType,
        filterset_class=EmployeeFilter)
    employee_by_id = graphene.Field(EmployeeType, id=graphene.Int())
    # 🔹 Advanced Queries
    employees_by_department = graphene.List(
        EmployeeType,
        department=graphene.String(required=True)
    )
    search_employees = graphene.List(
        EmployeeType,
        keyword=graphene.String(required=True)
    )
    employees_by_salary_range = graphene.List(
        EmployeeType,
        min_salary=graphene.Int(),
        max_salary=graphene.Int()
    )
    # 🔹 Resolvers
    def resolve_all_employees(root, info):
        return Employee.objects.all()

    def resolve_employee_by_id(root, info, id):
        return Employee.objects.get(id=id)

    def resolve_employees_by_department(root, info, department):
        return Employee.objects.filter(department__iexact=department)

    def resolve_search_employees(root, info, keyword):
        return Employee.objects.filter(name__icontains=keyword)

    def resolve_employees_by_salary_range(root, info, min_salary=0, max_salary=1000000):
        return Employee.objects.filter(
            salary__gte=min_salary,
            salary__lte=max_salary
        )
class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeType)
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        department = graphene.String(required=True)
        salary = graphene.Int(required=True)
    def mutate(self, info, name, email, department, salary):
        employee = Employee(
            name=name,
            email=email,
            department=department,
            salary=salary
        )
        employee.save()
        return CreateEmployee(employee=employee)
# 4️⃣ Update Employee
class UpdateEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeType)
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        department = graphene.String()
        salary = graphene.Int()
    def mutate(self, info, id, name=None, department=None, salary=None):
        employee = Employee.objects.get(id=id)
        if name:
            employee.name = name
        if department:
            employee.department = department
        if salary:
            employee.salary = salary
        employee.save()
        return UpdateEmployee(employee=employee)
# 5️⃣ Delete Employee
class DeleteEmployee(graphene.Mutation):
    success = graphene.Boolean()
    class Arguments:
        id = graphene.Int(required=True)
    def mutate(self, info, id):
        Employee.objects.get(id=id).delete()
        return DeleteEmployee(success=True)
# 6️⃣ Register Mutations
class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()