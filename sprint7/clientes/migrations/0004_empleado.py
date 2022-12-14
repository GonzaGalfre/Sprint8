# Generated by Django 4.1 on 2022-09-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_delete_clienttype_cliente_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': True,
            },
        ),
    ]
