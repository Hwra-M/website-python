# Generated by Django 2.2.20 on 2021-05-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
                ('offer', models.TextField(default='no offer')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
