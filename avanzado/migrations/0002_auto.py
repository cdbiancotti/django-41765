# Generated by Django 4.1.1 on 2022-10-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('cant_puertas', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('chasis', models.CharField(max_length=20)),
            ],
        ),
    ]
