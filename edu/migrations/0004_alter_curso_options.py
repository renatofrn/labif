# Generated by Django 3.2.8 on 2021-10-08 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_auto_20211007_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ('id', 'ativo'), 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]