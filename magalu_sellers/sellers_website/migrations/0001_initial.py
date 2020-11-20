from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('marca_produto', models.CharField(max_length=100)),
                ('categoria_produto', models.CharField(max_length=100)),
                ('preco_produto', models.FloatField()),
                ('quantidade_produto', models.FloatField()),
                ('imagem_produto', models.FileField(upload_to='')),
                ('complete', models.BooleanField(default=False)),
                ('vendedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sellers_website.vendedor')),
            ],
        ),
    ]
