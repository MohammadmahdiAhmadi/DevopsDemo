# Generated by Django 3.1.3 on 2021-02-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_idea_views'),
        ('users', '0002_auto_20201209_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='blog.Idea'),
        ),
    ]