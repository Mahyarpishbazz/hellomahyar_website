# Generated by Django 5.0.2 on 2024-02-19 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProject', '0008_blogindex_date1_alter_blogindex_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindex',
            name='date1',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False),
        ),
    ]
