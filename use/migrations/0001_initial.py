# Generated by Django 3.2.9 on 2021-11-19 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='areas.area')),
            ],
            options={
                'db_table': 'deers',
            },
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_lat', models.DecimalField(decimal_places=20, max_digits=30)),
                ('end_lng', models.DecimalField(decimal_places=20, max_digits=30)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('deer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='use.deer')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
            options={
                'db_table': 'use',
            },
        ),
    ]
