# Generated by Django 3.2.7 on 2022-01-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20170603_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='catagory',
            field=models.CharField(choices=[('sports', 'Тест на знание футбола'), ('movies', 'Кино'), ('maths', 'Тест по математике'), ('generalknowledge', 'Новогодний тест')], max_length=20),
        ),
    ]
