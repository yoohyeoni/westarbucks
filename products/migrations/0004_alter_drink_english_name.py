# Generated by Django 3.2.9 on 2021-11-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_drink_desciption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='english_name',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
