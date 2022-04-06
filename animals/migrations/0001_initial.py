# Generated by Django 4.0.3 on 2022-03-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('type', models.CharField(default='', max_length=50)),
                ('species', models.CharField(default='', max_length=50)),
                ('sound', models.CharField(default='', max_length=50)),
                ('image', models.CharField(default='', max_length=200)),
                ('sound_url', models.CharField(default='', max_length=200)),
                ('biome', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
