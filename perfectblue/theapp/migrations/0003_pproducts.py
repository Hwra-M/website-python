# Generated by Django 2.2.20 on 2021-05-25 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='PProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcname', models.CharField(max_length=100)),
                ('pcadd1', models.CharField(max_length=100)),
                ('pcmobile', models.TextField()),
            ],
        ),
    ]
