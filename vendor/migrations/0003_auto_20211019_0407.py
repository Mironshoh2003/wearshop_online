# Generated by Django 3.2.8 on 2021-10-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('-name',)},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='maxsulot narxi'),
        ),
    ]
