# Generated by Django 2.0.7 on 2019-04-07 03:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190407_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('TextField', tinymce.models.HTMLField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('News_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
        ),
    ]
