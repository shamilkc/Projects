# Generated by Django 4.1 on 2022-12-28 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_comment_image_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
