# Generated by Django 3.1 on 2021-01-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dateadvert',
            options={'ordering': ['id'], 'verbose_name': 'Срок', 'verbose_name_plural': 'Сроки'},
        ),
        migrations.AlterModelOptions(
            name='filteradvert',
            options={'ordering': ['id'], 'verbose_name': 'Фильтр', 'verbose_name_plural': 'Фильтры'},
        ),
        migrations.AlterField(
            model_name='advert',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
