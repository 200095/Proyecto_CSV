# Generated by Django 4.1.3 on 2023-03-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=255, unique=True)),
                ('Mensaje', models.CharField(max_length=1000)),
            ],
        ),
    ]