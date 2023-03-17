from django.db import models
from django.urls import reverse
from django.utils import timezone


class Info(models.Model):
    title = models.CharField(max_length = 100, null=True)
    date_time = models.DateTimeField(default = timezone.now, null=True)
    thumbnail = models.ImageField(default = 'default.jpg', upload_to = 'pics', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list_todos')

class Todo(models.Model):
    creater = models.ForeignKey(Info, on_delete = models.CASCADE, null=True,
                            related_name = 'todos')
    todo_content = models.CharField( max_length = 200, null=True)

    def __str__(self):
        return self.todo_content

    def get_absolute_url(self):
        return reverse('todos_detail', args[str(self.id)])
