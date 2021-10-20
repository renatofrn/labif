from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from edu.models import Matricula
from .models import Aluno
from django.core.paginator import Paginator#, EmptyPage, PageNotAnInteger
from .forms import AlunoForm, UserForm

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco.')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'login realizado com sucesso.')
                return redirect('dashboard')
            else:
                messages.error(request, 'falha na autenticação.')
                return redirect('login')
        else:
            messages.error(request, 'E-mail não cadastrado.')
            return redirect('login')
    else:
        return render(request, 'comum/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST["nome"]
        sobrenome = request.POST["sobrenome"]
        telefone = request.POST["telefone"]
        email = request.POST["email"]
        cpf = request.POST["cpf"]
        sexo = request.POST["sexo"]
        data_nascimento = request.POST["data_nascimento"]
        senha = request.POST["senha"]
        senha2 = request.POST["senha2"]

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(sobrenome):
            messages.error(request, 'O campo sobrenome não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(telefone):
            messages.error(request, 'O campo telefone não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(data_nascimento):
            messages.error(request, 'O campo Data de Nascimento não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(cpf):
            messages.error(request, 'O campo CPF não pode ficar em branco.')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais.')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('cadastro')
        if User.objects.filter(username=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return redirect('cadastro')
        user = User.objects.create_user(username=cpf, email=email, password=senha, first_name=nome, last_name=sobrenome)
        aluno = Aluno.objects.create(data_nascimento=data_nascimento, sexo=sexo, telefone=telefone, user=user)
        user.save()
        aluno.save()
        messages.error(request, 'Usuário cadastrado com sucesso.')
        return redirect('login')
    else:
        return render(request, 'comum/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        '''if Aluno.objects.filter(user_id=request.user.id).exists():'''
        matriculas = Matricula.objects.order_by('-data_matricula').filter(aluno_id=request.user.aluno.id)
        paginator = Paginator(matriculas, 3)
        page = request.GET.get('page')
        matriculas_por_pagina = paginator.get_page(page)
        dados = {
            'matriculas': matriculas_por_pagina,
        }
        return render(request, 'comum/dashboard.html', dados)
        '''else:
            messages.error(request, '')
            return redirect('index')'''
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.split();

def perfil(request):
    return render(request, 'comum/perfil.html')

def editar_perfil(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        aluno = get_object_or_404(Aluno, user_id=request.user.id)
        user.first_name = request.POST['nome']
        user.last_name = request.POST['sobrenome']
        user.email = request.POST['email']
        aluno.telefone = request.POST['telefone']
        aluno.data_nascimento = request.POST['data_nascimento']
        user.username = request.POST['cpf']
        aluno.sexo = request.POST['sexo']
        if 'foto_aluno' in request.FILES:
            aluno.foto_aluno = request.FILES['foto_aluno']
        user.save()
        aluno.save()
        messages.success(request, 'Perfil atualizado com sucesso.')
        return redirect('perfil')
    else:
        redirect('index')

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2

def cadastro_form(request):
    form_user = UserForm()
    form_aluno = AlunoForm()
    contexto = {
        'form_user': form_user,
        'form_aluno': form_aluno,
    }
    return render(request, 'comum/cadastro_form.html', contexto)

def confirma_cadastro_form(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_aluno = AlunoForm(request.POST)
        contexto = {
            'form_user': form_user,
            'form_aluno': form_aluno,
        }
        if form_aluno.is_valid() and form_user.is_valid():
            username = form_user.cleaned_data.get('username')
            email = form_user.cleaned_data.get('email')
            password = form_user.cleaned_data.get('password')
            first_name = form_user.cleaned_data.get('first_name')
            last_name = form_user.cleaned_data.get('last_name')
            data_nascimento = form_aluno.cleaned_data.get('data_nascimento')
            sexo = form_aluno.cleaned_data.get('sexo')
            telefone = form_aluno.cleaned_data.get('telefone')
            numero_rg = form_aluno.cleaned_data.get('numero_rg')
            uf_emissao_rg = form_aluno.cleaned_data.get('uf_emissao_rg')
            data_expedicao = form_aluno.cleaned_data.get('data_expedicao')
            #print(username,email,password,first_name,last_name,data_nascimento,sexo,telefone, numero_rg, uf_emissao_rg, data_expedicao)

            user = User.objects.create_user(username=username,
                                            email=email, 
                                            password=password, 
                                            first_name=first_name,
                                            last_name=last_name)
            aluno = Aluno.objects.create(data_nascimento=data_nascimento, 
                                         sexo=sexo, 
                                         telefone=telefone,
                                         numero_rg=numero_rg,
                                         uf_emissao_rg=uf_emissao_rg,
                                         data_expedicao=data_expedicao,
                                         user=user)
            user.save()
            aluno.save()

            messages.success(request, 'Usuário cadastrado com sucesso.')
            return render(request, 'comum/confirma_cadastro_form.html', contexto)
        else:
            return render(request, 'comum/cadastro_form.html', contexto)
    else:
        return redirect('cadastro_form')


'''def cadastro(request):
    if request.method == 'POST':
        

        
    else:
        return render(request, 'comum/cadastro.html')'''