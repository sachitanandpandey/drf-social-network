# Generated by Django 2.2.2 on 2019-06-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20190522_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Publication Date'),
        ),
    ]