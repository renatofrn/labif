from django.contrib import admin
from comum.models import Aluno

class AdminAlunos(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'user__first_name', 'user__first_name', 'cpf')
    list_per_page = 10

admin.site.register(Aluno, AdminAlunos)

