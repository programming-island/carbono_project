# Generated by Django 4.2.4 on 2023-08-18 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_tipoimovel_imovel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='foto',
            field=models.ImageField(default='default.jpg', upload_to='imoveis/', verbose_name='Foto do Imóvel'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='cidade',
            field=models.CharField(max_length=100, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço do Imóvel'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='qtd_banheiros',
            field=models.IntegerField(verbose_name='Qtd Banheiros'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='qtd_comodos',
            field=models.IntegerField(verbose_name='Qtd Comodos Totais'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='qtd_quartos',
            field=models.IntegerField(verbose_name='Qtd Quartos'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='tipo_imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.tipoimovel', verbose_name='Tipo do Imóvel'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título do Imóvel'),
        ),
    ]