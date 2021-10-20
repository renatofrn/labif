from django import forms
from django.forms import PasswordInput #, DateInput
from tempus_dominus.widgets import DatePicker
from comum.validations import *
from datetime import date
from comum.models import Aluno
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password2 = forms.CharField(max_length=30, required=True, label='Confirme a senha', widget=PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'CPF',
            'email': 'E-mail',
            'password': 'Senha'
            }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(first_name, last_name, email, username)
        lista_de_erros = {}
        possui_apenas_numeros(username, 'username', lista_de_erros)
        campo_form_vazio(first_name, 'first_name', lista_de_erros)
        campo_form_vazio(last_name, 'last_name', lista_de_erros)
        campo_form_vazio(email, 'email', lista_de_erros)
        campo_form_vazio(username, 'username', lista_de_erros)
        email_ja_cadastrado(email, lista_de_erros)
        cpf_ja_cadastrado(username, lista_de_erros)
        senhas_nao_sao_iguais(password, password2, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_de_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_de_erro)
        return self.cleaned_data


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
            'numero_rg': 'Número do RG',
            'uf_emissao_rg': 'UF de emissão do RG',
            'data_expedicao': 'Data de expedição do RG',
            'data_nascimento': 'Data de nascimento',
            'sexo': 'Sexo',
            'telefone': 'Telefone',
            }
        widgets = {
            'data_expedicao': DatePicker(),
            'data_nascimento': DatePicker(),
        }
        exclude = {'user', 'foto_aluno'}

        '''fields = ['numero_rg',
                  'uf_emissao_rg',
                  'data_expedicao',
                  'data_nascimento',
                  'sexo',
                  'telefone']'''


    '''ESTADO_OPCOES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas" ),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    SEXO_OPCOES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    )'''

    '''numero_rg = forms.CharField(max_length=100, required=True, label='Número do RG')
    uf_emissao_rg = forms.ChoiceField(choices=ESTADO_OPCOES, label='UF Emissora do RG')
    data_expedicao = forms.DateField(label="Data de expedição", widget=DatePicker())
    data_nascimento = forms.DateField(label="Data de nascimento", widget=DatePicker())
    sexo = forms.ChoiceField(choices=SEXO_OPCOES, label='Sexo')
    telefone = forms.CharField(max_length=100, required=True, label='Telefone')'''

    '''def clean_numero_rg(self):
        numero_rg = self.cleaned_data.get('numero_rg')
        if any(not char.isdigit() for char in numero_rg):
            raise forms.ValidationError('Número RG inválido: Inclua somente números.')
        else:
            print('numero_rg')
            return numero_rg

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if any(not char.isdigit() for char in telefone):
            raise forms.ValidationError('Número de telefone inválido: Inclua somente números.')
        else:
            print('telefone')
            return telefone'''

    def clean(self):
        numero_rg = self.cleaned_data.get('numero_rg')
        telefone = self.cleaned_data.get('telefone')
        data_expedicao = self.cleaned_data.get('data_expedicao')
        data_nascimento = self.cleaned_data.get('data_nascimento')
        lista_de_erros = {}
        possui_apenas_numeros(numero_rg, 'numero_rg', lista_de_erros)
        possui_apenas_numeros(telefone, 'telefone', lista_de_erros)
        hoje = date.today()
        data_menor_que_hoje(data_expedicao, 'data_expedicao', hoje, lista_de_erros)
        data_menor_que_hoje(data_nascimento, 'data_nascimento', hoje, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_de_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_de_erro)
        return self.cleaned_data


    '''logradouro = forms.CharField(max_length=255, required=True, label='Logradouro')
    numero = forms.CharField(max_length=20, required=True, label='Número')
    complemento = forms.CharField(max_length=255, required=False, label='Complemento')
    bairro = forms.CharField(max_length=255, required=True, label='Bairro')
    cidade = forms.CharField(max_length=255, required=True, label='Cidade')
    cep = forms.CharField(max_length=10, required=False, label='CEP')'''



