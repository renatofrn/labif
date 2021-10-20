from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db import models


class Curso(models.Model):

    PERIODICIDADE_CHOICES = [
        [1, 'Anual'],
        [2, 'Semestral'],
        [3, 'Livre']]

    TIPO_HORA_AULA_CHOICES = [
        [45, '45 min'],
        [60, '60 min']
    ]

    codigo = models.CharField(verbose_name='Código do Curso',
                              help_text='Código usado para composição de turmas e matrículas', unique=True, max_length=10)
    descricao = models.CharField(verbose_name='Descrição', max_length=500, null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    ppc = models.FileField(upload_to='static/', null=True, blank=True, verbose_name='PPC', default=None)
    ch_total = models.PositiveIntegerField('Carga Horária Total do Curso', blank=True, null=True, default=None)
    tipo_hora_aula = models.PositiveIntegerField('Tipo Hora Aula', blank=True, null=True,
                                                 choices=TIPO_HORA_AULA_CHOICES)
    periodicidade = models.PositiveIntegerField('Periodicidade', choices=PERIODICIDADE_CHOICES, null=True)
    media_aprovacao = models.DecimalField('Média para aprovação', null=True, blank=True,
                                          help_text='Valor entre 0 e 10.', decimal_places=2, max_digits=5,
                                          validators=[MinValueValidator(Decimal(0)),
                                                      MaxValueValidator(Decimal(10))])
    conteudo = models.TextField(verbose_name='Conteúdo')
    imagem_curso = models.ImageField(upload_to='img_cursos/%Y/%m/%d/', blank=True)


    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering =('id', 'ativo',)

    def __str__(self):
        codigo = self.codigo.replace('-', '')
        return '{} - {}'.format(codigo, self.descricao)

class Matricula(models.Model):

    aluno = models.ForeignKey('comum.Aluno', verbose_name='Aluno', related_name='comum_aluno', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', verbose_name='Curso', related_name='edu_curso', on_delete=models.CASCADE)
    matricula = models.IntegerField()
    observacao = models.TextField()
    data_matricula = models.DateTimeField(verbose_name='Data da matrícula', blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Matricula de Aluno'
        verbose_name_plural = 'Matriculas de Alunos'
        ordering = ["matricula"]

    def __str__(self):
        return '{} - {}'.format(self.matricula, self.aluno)