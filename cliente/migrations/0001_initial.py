# Generated by Django 3.1.1 on 2020-10-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('sobrenome', models.CharField(max_length=25)),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('mostrar', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
    ]
