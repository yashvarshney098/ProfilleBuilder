# Generated by Django 4.2.2 on 2023-07-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='dsf', max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
    ]
