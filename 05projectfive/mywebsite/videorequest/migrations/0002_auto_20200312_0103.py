# Generated by Django 3.0.4 on 2020-03-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videotitle',
            field=models.CharField(max_length=30),
        ),
    ]
