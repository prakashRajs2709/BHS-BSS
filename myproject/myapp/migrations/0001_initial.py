# Generated by Django 5.1.6 on 2025-02-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FA1',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('slno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('eng', models.IntegerField()),
                ('kan', models.IntegerField()),
                ('hin', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('sci', models.IntegerField()),
                ('soc_sci', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FA2',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('slno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('eng', models.IntegerField()),
                ('kan', models.IntegerField()),
                ('hin', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('sci', models.IntegerField()),
                ('soc_sci', models.IntegerField()),
            ],
        ),
    ]
