# Generated by Django 4.1.7 on 2023-03-07 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0010_card_position_alter_card_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 8, 18, 53, 21, 211038)),
        ),
    ]
