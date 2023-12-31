# Generated by Django 4.2.2 on 2023-07-16 12:13

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, null=True)),
                ('firstname', models.CharField(default=None, max_length=100, null=True)),
                ('lastname', models.CharField(default=None, max_length=100, null=True)),
                ('password', models.CharField(default=None, max_length=100, null=True)),
                ('phone', models.CharField(default=None, max_length=100, null=True)),
                ('profileimage', models.FileField(upload_to='media/images/')),
                ('gradyear', models.IntegerField(default=None, null=True)),
                ('posprimary', models.CharField(default=None, max_length=100, null=True)),
                ('possecondary', models.CharField(default=None, max_length=100, null=True)),
                ('instagram', models.CharField(default=None, max_length=1000, null=True)),
                ('twitter', models.CharField(default=None, max_length=1000, null=True)),
                ('facebook', models.CharField(default=None, max_length=1000, null=True)),
                ('school', models.CharField(default=None, max_length=100, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('state', models.CharField(default=None, max_length=100, null=True)),
                ('ncaa', models.CharField(default=None, max_length=100, null=True)),
                ('height', models.CharField(default=None, max_length=100, null=True)),
                ('weight', models.CharField(default=None, max_length=100, null=True)),
                ('vertical', models.CharField(default=None, max_length=100, null=True)),
                ('time40', models.CharField(default=None, max_length=100, null=True)),
                ('gpa', models.CharField(default=None, max_length=100, null=True)),
                ('actscore', models.CharField(default=None, max_length=100, null=True)),
                ('satscore', models.CharField(default=None, max_length=100, null=True)),
                ('classrank', models.CharField(default=None, max_length=100, null=True)),
                ('url1', models.CharField(default=None, max_length=1000, null=True)),
                ('url2', models.CharField(default=None, max_length=1000, null=True)),
                ('sbp1', models.CharField(default=None, max_length=1000, null=True)),
                ('sbp2', models.CharField(default=None, max_length=1000, null=True)),
                ('sbp3', models.CharField(default=None, max_length=1000, null=True)),
                ('sbp4', models.CharField(default=None, max_length=1000, null=True)),
                ('abp1', models.CharField(default=None, max_length=1000, null=True)),
                ('abp2', models.CharField(default=None, max_length=1000, null=True)),
                ('abp3', models.CharField(default=None, max_length=1000, null=True)),
                ('abp4', models.CharField(default=None, max_length=1000, null=True)),
                ('s1date', models.CharField(default=None, max_length=1000, null=True)),
                ('s1location', models.CharField(default=None, max_length=1000, null=True)),
                ('s1event', models.CharField(default=None, max_length=1000, null=True)),
                ('s2date', models.CharField(default=None, max_length=1000, null=True)),
                ('s2location', models.CharField(default=None, max_length=1000, null=True)),
                ('s2event', models.CharField(default=None, max_length=1000, null=True)),
                ('s3date', models.CharField(default=None, max_length=1000, null=True)),
                ('s3location', models.CharField(default=None, max_length=1000, null=True)),
                ('s3event', models.CharField(default=None, max_length=1000, null=True)),
                ('coachmessage', models.CharField(default=None, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
