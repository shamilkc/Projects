# Generated by Django 4.1 on 2022-09-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_categoryclass_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]