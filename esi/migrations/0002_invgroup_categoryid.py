# Generated by Django 2.1.2 on 2019-01-09 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invgroup',
            name='categoryID',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]