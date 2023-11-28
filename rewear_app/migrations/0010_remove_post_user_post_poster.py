# Generated by Django 4.2.7 on 2023-11-28 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rewear_app', '0009_remove_post_poster_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rewear_app.poster'),
        ),
    ]
