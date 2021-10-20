from django.contrib.auth.models import User


def possui_apenas_numeros(valor_campo, nome_campo, lista_de_erros):
    """Verifica se o campo possui apenas números"""
    if any(not char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Permitido apenas números neste campo.'

def data_menor_que_hoje(campo_data, nome_campo, data_atual, lista_de_erros):
    """Verifica se a data inserida é menor que a data de hoje"""
    if campo_data > data_atual:
        lista_de_erros[nome_campo] = 'A data inserida deve ser menor que a data de hoje.'

def campo_form_vazio(valor_campo, nome_campo, lista_de_erros):
    """Verifica se o campo do formulário  é vazio"""
    if not valor_campo.split():
        lista_de_erros[nome_campo] = 'Este campo não pode ser vazio.'

def email_ja_cadastrado(email, lista_de_erros):
    """Verifica se o email já está cadastrado no banco de dados """
    if User.objects.filter(email=email).exists():
        lista_de_erros['email'] = 'Este email já está cadastrado no sistema.'

def cpf_ja_cadastrado(cpf, lista_de_erros):
    """Verifica se o CPF (username) já está cadastrado no banco de dados """
    if User.objects.filter(username=cpf).exists():
        lista_de_erros['username'] = 'Este CPF já está cadastrado no sistema.'

def senhas_nao_sao_iguais(password, password2, lista_de_erros):
    """Verifica se o campo é vazio"""
    if password != password2:
        lista_de_erros['password2'] = 'A senha e a sua confirmação devem ser iguais.'


'''
ESTADOS = (
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
    )'''