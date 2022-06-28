# Generated by Django 4.0.4 on 2022-06-15 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_product_name_notes_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.notes'),
        ),
        migrations.AddField(
            model_name='cart',
            name='photo',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]