# Generated by Django 4.1.7 on 2023-03-10 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0015_rename_list_cardslist_alter_card_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 22, 17, 21, 691444)),
        ),
    ]