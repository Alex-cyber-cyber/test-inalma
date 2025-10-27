
from django.db import migrations, models
from django.db.models.functions import Lower

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tags', models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(Lower('name'), name='uniq_product_name_ci'),
        ),
    ]
