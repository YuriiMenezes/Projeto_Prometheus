# Generated by Django 3.2.9 on 2021-11-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='nome_comentario',
            field=models.CharField(max_length=150, verbose_name='Nome do Comentario'),
        ),
    ]