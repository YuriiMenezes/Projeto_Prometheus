# Generated by Django 3.2.9 on 2021-11-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0004_auto_20211104_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerto_post',
            field=models.TextField(verbose_name='Sumário'),
        ),
    ]