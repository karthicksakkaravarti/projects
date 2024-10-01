# Generated by Django 4.0.8 on 2023-09-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='installedapp',
            name='author',
            field=models.CharField(default='Karthick', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installedapp',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='installedapp',
            name='other',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installedapp',
            name='version',
            field=models.CharField(default='1.0.0', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='installedapp',
            name='app_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Addons Name'),
        ),
        migrations.AlterField(
            model_name='installedapp',
            name='is_installed',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
    ]
