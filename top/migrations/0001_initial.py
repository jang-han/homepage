# Generated by Django 3.2.9 on 2022-02-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ingredient1', models.CharField(max_length=20)),
                ('ingredient2', models.CharField(max_length=20)),
                ('ingredient3', models.CharField(max_length=20)),
                ('ingredient4', models.CharField(max_length=20)),
                ('ingredient5', models.CharField(max_length=20)),
                ('course', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('regist', models.DateField()),
                ('update', models.DateField()),
            ],
        ),
    ]
