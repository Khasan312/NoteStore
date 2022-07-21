# Generated by Django 4.0.5 on 2022-07-18 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_color_notebook_image_alter_notebook_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='notebook',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebook.brand'),
        ),
    ]
