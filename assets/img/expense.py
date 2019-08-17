from ariadne import gql, ObjectType

from .query import query
from ..utils.ariadne_utils import convert_kwargs_to_snake_case
from ..services.expense_service import list_expenses, get_expense, get_expense_category, list_expense_categories
from ..services.provider_service import get_provider

type_defs = gql("""
    type Expense {
        id: ID!
        budget: Budget!
        provider: Provider!
        providerReference: String!
        category: ExpenseCategory!
        type: ExpenseType!
        title: String!
        amount: Int!
        justification: String
        expensedOn: Datetime!
        startedOn: Datetime
        endedOn: Datetime
        createdOn: Datetime!
        updatedOn: Datetime
    }
    type ExpenseList {
        items: [Expense]!,
        count: Int!
    }
    enum ExpenseType {
        PRO
        PRIVATE
    }
""")

expense = ObjectType('Expense')


@query.field("expense")
@convert_kwargs_to_snake_case
def resolve_expense(_, info, **arguments):
    return get_expense(arguments['id'])


@query.field("expenses")
@convert_kwargs_to_snake_case
def resolve_expenses(_, info, **arguments):
    expenses, expenses_count = list_expenses(**arguments)

    return {
        "items": expenses,
        "count": expenses_count
    }


@expense.field("category")
@convert_kwargs_to_snake_case
def resolve_expense_category(_, info, **arguments):
    return get_expense_category(arguments['id'])


@expense.field('type')
@convert_kwargs_to_snake_case
async def resolve_type(node, *_):
    return node.type.upper()


@expense.field("provider")
@convert_kwargs_to_snake_case
def resolve_provider(node, *_):
    return get_provider(node.provider_id)


@expense.field("category")
@convert_kwargs_to_snake_case
def resolve_provider(node, *_):
    return get_expense_category(node.category_id)
