# Generated by Django 2.2.5 on 2020-03-15 01:58

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200314_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_path_file, verbose_name='Imagem'),
        ),
    ]
