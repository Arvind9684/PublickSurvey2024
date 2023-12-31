# Generated by Django 4.2.8 on 2023-12-28 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_chat_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='public_votting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('party_name', models.CharField(max_length=50)),
                ('Latitude', models.CharField(max_length=50)),
                ('Longitude', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=10)),
                ('mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.contact_detail')),
            ],
        ),
    ]
