# Generated by Django 2.2.5 on 2020-01-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostResultsCell',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_active_material', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cat_binder', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cat_conductor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('an_active_material', models.DecimalField(decimal_places=2, max_digits=20)),
                ('an_binder', models.DecimalField(decimal_places=2, max_digits=20)),
                ('an_conductor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('al_foil', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cu_foil', models.DecimalField(decimal_places=2, max_digits=20)),
                ('can', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sep', models.DecimalField(decimal_places=2, max_digits=20)),
                ('elyte', models.DecimalField(decimal_places=2, max_digits=20)),
                ('manufacturing', models.DecimalField(decimal_places=2, max_digits=20)),
                ('pack_integration', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'cost_results_cell',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CostResultsInfo',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_version', models.DecimalField(decimal_places=2, max_digits=20)),
                ('date_created', models.DateTimeField()),
                ('cell_id', models.PositiveIntegerField()),
                ('price_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'cost_results_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CostResultsKwh',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_active_material', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cat_binder', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cat_conductor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('an_active_material', models.DecimalField(decimal_places=2, max_digits=20)),
                ('an_binder', models.DecimalField(decimal_places=2, max_digits=20)),
                ('an_conductor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('al_foil', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cu_foil', models.DecimalField(decimal_places=2, max_digits=20)),
                ('can', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sep', models.DecimalField(decimal_places=2, max_digits=20)),
                ('elyte', models.DecimalField(decimal_places=2, max_digits=20)),
                ('manufacturing', models.DecimalField(decimal_places=2, max_digits=20)),
                ('pack_integration', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'cost_results_kwh',
                'managed': True,
            },
        ),
    ]
