# Generated by Django 4.2.1 on 2023-07-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
            ],
            options={
                'db_table': 'prodcut',
            },
        ),
    ]
