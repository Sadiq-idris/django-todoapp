from django.urls import path
from .views import (DeleteListTodoView, HomePageView,
                    CreateTodo, TodosDetail, ListTodoInfo,
                    DeleteInfo
)


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('delete/<int:pk>', DeleteListTodoView.as_view(), name='delete_todo'),
    path('create/', CreateTodo.as_view(), name='create_todo'),
    path('detail/<int:pk>', TodosDetail.as_view(), name = 'todos_detail'),
    path('info/', ListTodoInfo.as_view(), name='list_todos'),
    path('delete/info/<int:pk>', DeleteInfo.as_view(), name='delete_info'),
]