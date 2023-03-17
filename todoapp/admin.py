from django.contrib import admin
from .models import Todo, Info

class TodoInline(admin.TabularInline):
    model = Todo

class InfoAdmin(admin.ModelAdmin):
    inlines = [
        TodoInline,
    ]


admin.site.register(Todo)

admin.site.register(Info, InfoAdmin)