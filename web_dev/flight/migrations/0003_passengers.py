# Generated by Django 3.1.2 on 2020-11-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20201103_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flight.flight')),
            ],
        ),
    ]