# Generated by Django 4.1.1 on 2022-10-25 00:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0002_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
