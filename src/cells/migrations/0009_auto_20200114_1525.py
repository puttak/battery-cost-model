# Generated by Django 2.2.5 on 2020-01-14 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0008_auto_20200114_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellinput',
            name='cell_name',
            field=models.CharField(db_column='cellName', error_messages={'unique': 'This cell_name is already taken.'}, max_length=45, unique=True),
        ),
    ]
