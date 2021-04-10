# Generated by Django 2.2.12 on 2021-04-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFeesDetail',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('reference_id_card_unique_number', models.PositiveIntegerField()),
                ('engineering_year', models.CharField(choices=[('FY', 'FIRST YEAR'), ('SY', 'SECOND YEAR'), ('TY', 'THIRD YEAR'), ('BY', 'BACHELOR YEAR')], default='BY', max_length=30)),
                ('batch', models.PositiveIntegerField(default=2020)),
                ('branch_choose', models.CharField(choices=[('IT', 'Information Technology'), ('ME', 'Mechanical Engineering'), ('CE', 'Computer Engineering'), ('ENTC', 'Electronic Engineering'), ('AE', 'Aerospace Engineering'), ('Chem E', 'Chemical Engineering'), ('Civil E', 'Civil Engineeing')], default='ME', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('fees_amount', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'studentfeesdetail',
            },
        ),
    ]