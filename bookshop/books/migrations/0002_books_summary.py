# Generated by Django 3.2.7 on 2021-09-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='summary',
            field=models.CharField(default='no summary', max_length=9999),
            preserve_default=False,
        ),
    ]
