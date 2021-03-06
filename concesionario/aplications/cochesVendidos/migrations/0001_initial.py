# Generated by Django 3.1.2 on 2020-10-15 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CochesVendidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('extras_instalados', models.CharField(max_length=50)),
                ('numero_puertas', models.IntegerField()),
                ('codigo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
        ),
    ]
