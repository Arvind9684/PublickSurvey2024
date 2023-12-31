# Generated by Django 4.2.8 on 2023-12-23 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_alter_contact_detail_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('Chat', models.CharField(max_length=500)),
                ('Latitude', models.CharField(max_length=50)),
                ('Longitude', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=10)),
                ('mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.contact_detail')),
            ],
        ),
    ]
