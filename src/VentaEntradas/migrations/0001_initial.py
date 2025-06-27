from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='TipoDNI',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nro_dni', models.IntegerField()),
                ('tipo_dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentaEntradas.TipoDNI')),
            ],
        ),
        migrations.CreateModel(
            name='MedioDePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentaEntradas.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('importe', models.DecimalField(max_digits=10, decimal_places=2)),
                ('medio_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentaEntradas.MedioDePago')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentaEntradas.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDeVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('cant_entradas', models.IntegerField()),
                ('importe_unitario', models.DecimalField(max_digits=10, decimal_places=2)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentaEntradas.Venta')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentaEntradas.Entrada')),
            ],
        ),
    ]
