# Generated by Django 2.0.6 on 2018-08-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='type',
            new_name='que_type',
        ),
        migrations.AlterField(
            model_name='examrecord',
            name='exam_count',
            field=models.IntegerField(default=1, verbose_name='count of exam'),
        ),
    ]