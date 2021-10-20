from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    ESTADO_OPCOES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
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
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=False)
    sexo = models.CharField(choices=SEXO_OPCOES, max_length=30, blank=False)
    telefone = models.CharField(verbose_name='Telefone', max_length=15, blank=False)
    foto_aluno = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=False)
    numero_rg = models.CharField(verbose_name='Número do RG', max_length=30, blank=False)
    uf_emissao_rg = models.CharField(choices=ESTADO_OPCOES, max_length=30, blank=False,)
    data_expedicao = models.DateField(verbose_name="Data de expedição", blank=False)

    '''
    logradouro = models.CharField(max_length=255, erbose_name='Logradouro')
    numero = models.CharField(max_length=20, verbose_name='Número')
    complemento = models.CharField(max_length=255, verbose_name='Complemento')
    bairro = models.CharField(max_length=255,  verbose_name='Bairro')
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    cep = models.CharField(max_length=10, verbose_name='CEP')
    '''

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ('user__first_name',)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
