# Generated by Django 3.0.8 on 2020-08-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20200803_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='lend_to',
            field=models.ManyToManyField(to='p_library.Friend'),
        ),
    ]
