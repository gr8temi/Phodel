# Generated by Django 2.0.7 on 2019-02-11 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to="'Users'+User"),
        ),
        migrations.AlterField(
            model_name='pcompany',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='pmodel',
            name='model_image',
            field=models.ImageField(blank=True, default='Users/Model/user.png', upload_to='Users/Model'),
        ),
        migrations.AddField(
            model_name='interest',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Pmodel'),
        ),
    ]
