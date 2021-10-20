from django.contrib import admin
from .models import Matricula, Curso


class AdminMatriculas(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'aluno')
    list_display_links = ('id', 'matricula', 'aluno')
    search_fields = ('nome_aluno', 'matricula')
    list_filter = ('curso',)
    list_per_page = 10

class AdminCursos(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'codigo', 'ativo')
    list_display_links = ('id', 'descricao', 'codigo')
    search_fields = ('descricao', 'codigo')
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Matricula, AdminMatriculas)
admin.site.register(Curso, AdminCursos)