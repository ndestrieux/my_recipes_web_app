# Generated by Django 4.1.3 on 2022-11-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_ingredient_recipes_recipe_recipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', through='app.IngredientQuantity', to='app.ingredient'),
        ),
    ]
