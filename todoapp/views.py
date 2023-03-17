from django.shortcuts import render
from django.views.generic import (CreateView, TemplateView,DetailView, ListView, FormView)
from django.views.generic.edit import DeleteView
from django.views.generic.detail import SingleObjectMixin
from .models import Todo, Info
from django.urls import reverse_lazy, reverse
from .forms import TodoForm
from django.views import View



class DeleteListTodoView(DeleteView):
    model = Todo
    template_name='delete_todo.html'
    success_url = reverse_lazy('list_todos')


class HomePageView(TemplateView):
    template_name = 'index.html'

class CreateTodo(CreateView):
    model = Info
    template_name = 'create_todo.html'
    fields = '__all__'


# DETAIL PAGE GET REQUEST 
class TodoGet(DetailView):
    model = Info
    template_name = 'detail_todos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = TodoForm()
        return context


# DETAIL PAGE POST REQUEST
class TodoPost(SingleObjectMixin, FormView):
    model = Info
    form_class = TodoForm
    template_name = 'detail_todos.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.creater = self.object
        todo.save()
        return super().form_valid(form)

    def get_success_url(self):
        info = self.get_object()
        return reverse('todos_detail', kwargs = {'pk':info.pk})
    

# DETAIL TODO VIEW 
class TodosDetail(View):
    def get(self, request, *args, **kwargs):
        view = TodoGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TodoPost.as_view()
        return view(request, *args, **kwargs)
    



class ListTodoInfo(ListView):
    model = Info
    template_name = 'list_info_todo.html'

class DeleteInfo(DeleteView):
    model = Info
    success_url = reverse_lazy('list_todos')
    template_name = 'info_delete.html'
    
