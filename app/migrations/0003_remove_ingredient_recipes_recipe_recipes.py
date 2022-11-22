# Generated by Django 4.1.3 on 2022-11-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_recipe_image_alter_recipe_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipes',
            field=models.ManyToManyField(related_name='ingredients', through='app.IngredientQuantity', to='app.ingredient'),
        ),
    ]
