# Generated by Django 3.2.4 on 2021-06-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]