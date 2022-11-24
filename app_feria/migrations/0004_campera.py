# Generated by Django 4.0.5 on 2022-11-24 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feria', '0003_alter_camisa_talle_alter_remera_talle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('talle', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
    ]
