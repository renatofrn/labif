import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Matricula, Curso
from comum.models import Aluno
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    cursos = Curso.objects.filter(ativo=True)
    paginator = Paginator(cursos, 3)
    page = request.GET.get('page')
    cursos_por_pagina = paginator.get_page(page)
    dados = {
        'cursos': cursos_por_pagina,
    }
    return render(request, 'index.html', dados)

'''def index(request):
    matriculas = Matricula.objects.all()
    cursos = Curso.objects.order_by('codigo').filter(ativo=True)
    dados = {
        'cursos': cursos,
        'matriculas': matriculas,
    }
    return render(request, 'index.html', dados)'''

def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    matriculado = False
    if request.user.is_authenticated and Matricula.objects.filter(aluno_id=request.user.aluno.id, curso_id=curso_id).exists():
        matriculado = True
    dados = {
        'curso': curso,
        'matriculado': matriculado,
    }
    return render(request, 'edu/curso.html', dados)

'''def edu(request, matricula_id):
    matricula = get_object_or_404(Matricula, pk=matricula_id)
    data_acesso = timezone.now()
    matricula_a_exibir = {
        'matricula': matricula,
        'data_acesso': data_acesso,
    }
    return render(request, 'edu.html', matricula_a_exibir)'''

def matricular_aluno(request, curso_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        aluno = get_object_or_404(Aluno, user_id=user_id)
        curso = get_object_or_404(Curso, pk=curso_id)
        if request.method == 'POST':
            observacao = request.POST['observacao']
            currentDateTime = datetime.datetime.now()
            year = currentDateTime.date().strftime("%Y")
            numero = '0000000000{}{}'.format(user_id, curso_id)
            num_matricula = '{}{}'.format(year, numero[-6:])
            matricula = Matricula.objects.create(aluno=aluno, curso=curso, matricula=num_matricula,
                                                 observacao=observacao)
            matricula.save()
            messages.success(request, 'Matrícula efetuada com sucesso')
            return redirect('dashboard')
        else:
            dados = {
                'aluno': aluno,
                'curso': curso,
            }
            return render(request, 'edu/matricular_aluno.html', dados)
    else:
        messages.error(request, 'Primeiro, realize o login.')
        return redirect('login')

'''
def matricular_aluno_form(request, curso_id):
    aluno = get_object_or_404(Aluno, user_id=request.user.id)
    curso = get_object_or_404(Curso, pk=curso_id)
    form = AlunoForm()
    contexto = {
        'form': form,
        'aluno': aluno,
        'curso': curso,
    }
    return render(request, 'comum/matricular_aluno_form.html', contexto)

'''

def desmatricular_aluno(request, curso_id):
    matricula = Matricula.objects.filter(curso_id=curso_id,aluno_id=request.user.aluno.id)
    matricula.delete()
    messages.success(request, 'Matrícula deletada com sucesso.')
    return redirect('dashboard')

def buscar(request):
    lista_cursos = Curso.objects.order_by('codigo').filter(ativo=True)
    if 'busca' in request.GET: #se buscar tem um valor nesta request
        dado_a_buscar = request.GET['busca'] #recebe o texto buscado
        print(dado_a_buscar)
        if buscar:

            lista_cursos = lista_cursos.filter(descricao__icontains=dado_a_buscar)
    print(lista_cursos)
    dados = {
        'cursos': lista_cursos,
    }
    return render(request, 'edu/buscar.html', dados)
