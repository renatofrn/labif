# Generated by Django 3.2.8 on 2021-10-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0004_alter_curso_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagem_curso',
            field=models.ImageField(blank=True, upload_to='img_cursos/%Y/%m/%d/'),
        ),
    ]
