# Generated by Django 3.1.3 on 2020-11-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers_website', '0005_produto_codigo_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem_produto',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]