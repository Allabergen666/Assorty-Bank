from django.contrib.auth.decorators import login_required
# Импортируем класс JsonResponse из модуля django.http, 
# чтобы создавать HTTP-ответы в формате JSON.
from django.http import JsonResponse
# Импортируем класс GraphQLView из модуля graphene_django.views, 
# который представляет представление Django для обработки запросов GraphQL.
from graphene_django.views import GraphQLView
# Импортируем переменную schema из модуля schema.py, которая содержит определение схемы GraphQL.
from .schema import schema  
from django.urls import path


class CustomGraphQLView(GraphQLView): 
    # Переопределяем метод execute_graphql_request, чтобы добавить дополнительную логику перед выполнением запроса GraphQL. 
    def execute_graphql_request(self, request, data, query, variables, operation_name, show_graphiql=False):
        return super().execute_graphql_request(
            request, data, query, variables, operation_name, show_graphiql
        )


@login_required(login_url='/login')
def graphql_view(request):
    # Создаем экземпляр CustomGraphQLView с передачей параметров graphiql=True и schema=schema.
    view = CustomGraphQLView.as_view(graphiql=True, schema=schema)
    # Вызываем представление view, передавая объект request для обработки запроса GraphQL.
    return view(request)


urlpatterns = [
    path('', graphql_view),
]