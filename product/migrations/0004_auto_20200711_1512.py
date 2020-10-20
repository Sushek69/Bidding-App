# Generated by Django 3.0.3 on 2020-07-11 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
