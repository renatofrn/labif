from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('curso/<int:curso_id>', views.curso, name='curso'),
    path('curso/matricular_aluno/<int:curso_id>', views.matricular_aluno, name='matricular_aluno'),
    path('curso/desmatricular_aluno/<int:curso_id>', views.desmatricular_aluno, name='desmatricular_aluno'),
    path('buscar', views.buscar, name='buscar'),
]
# path('<int:matricula_id>', views.edu, name='edu'),