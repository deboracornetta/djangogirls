# Generated by Django 3.1.3 on 2020-11-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers_website', '0010_auto_20201120_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.ImageField(default='images/products/img.png', upload_to='images/products'),
        ),
    ]
