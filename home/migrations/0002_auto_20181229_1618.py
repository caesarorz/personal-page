# Generated by Django 2.1.1 on 2018-12-29 16:18

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jumbotron',
            old_name='title_description',
            new_name='paragraph',
        ),
        migrations.RemoveField(
            model_name='jumbotron',
            name='title',
        ),
        migrations.AddField(
            model_name='jumbotron',
            name='header_one',
            field=models.CharField(default='Hello World', max_length=220),
        ),
        migrations.AddField(
            model_name='jumbotron',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.upload_image_path),
        ),
    ]