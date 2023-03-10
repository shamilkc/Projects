# Generated by Django 4.1 on 2023-01-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
