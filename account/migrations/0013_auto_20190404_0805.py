# Generated by Django 2.0.7 on 2019-04-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20190221_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
