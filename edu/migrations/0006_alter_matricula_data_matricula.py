# Generated by Django 3.2.8 on 2021-10-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0005_curso_imagem_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='data_matricula',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da matrícula'),
        ),
    ]
