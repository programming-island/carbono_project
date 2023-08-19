# Generated by Django 4.2.4 on 2023-08-19 15:32

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_imovel_foto_fotosdosimoveis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fotosdosimoveis',
            options={'verbose_name': 'Foto do Imóvel', 'verbose_name_plural': 'Fotos dos Imóveis'},
        ),
        migrations.AlterField(
            model_name='fotosdosimoveis',
            name='foto',
            field=models.ImageField(upload_to=website.models.upload_to),
        ),
    ]