# Generated by Django 4.2.4 on 2023-08-18 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(verbose_name=100)),
                ('qtd_quartos', models.IntegerField()),
                ('qtd_banheiros', models.IntegerField()),
                ('qtd_comodos', models.IntegerField()),
                ('tipo_imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.tipoimovel')),
            ],
        ),
    ]
