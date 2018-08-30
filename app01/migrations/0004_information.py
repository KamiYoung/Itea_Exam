# Generated by Django 2.0.6 on 2018-08-30 03:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180830_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ch_name', models.CharField(max_length=128, verbose_name='chinese')),
                ('en_name', models.CharField(max_length=128, verbose_name='english')),
                ('info_type', models.IntegerField(choices=[(1, 'Commonly Use Words'), (2, 'Commonly Use Words Menu')], default=1)),
                ('file_path', models.CharField(max_length=256)),
                ('file_name', models.CharField(max_length=64)),
            ],
        ),
    ]