from django.db import migrations


def create_data(apps, schema_editor):
    Produto = apps.get_model('produtos', 'Produto')
    Produto(nome="Produto 1", preco=125.80,
            descricao="Descrição teste.").save()


class Migration(migrations.Migration):
    dependencies = [
        ('produtos', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
