# Generated by Django 5.0.2 on 2024-02-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProject', '0004_blogindexb_blogindexbb'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexbbb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mystamp', models.DateTimeField(auto_now_add=True, verbose_name='When Created')),
            ],
        ),
    ]
