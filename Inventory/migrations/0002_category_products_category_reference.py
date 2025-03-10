# Generated by Django 5.1.4 on 2024-12-23 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='category_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.category'),
        ),
    ]
