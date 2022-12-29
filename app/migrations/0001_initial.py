# Generated by Django 4.1.3 on 2022-12-29 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="IngredientQuantity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "unit",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ml", "milliliter"),
                            ("l", "liter"),
                            ("tsp", "teaspoon"),
                            ("tbsp", "tablespoon"),
                            ("mg", "milligram"),
                            ("g", "gram"),
                            ("kg", "kilogram"),
                            ("lb", "pound"),
                            ("oz", "ounce"),
                            ("piece", "piece"),
                        ],
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app.ingredient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MailLogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("recipient", models.EmailField(max_length=254)),
                ("recipe_id", models.IntegerField(blank=True, null=True)),
                ("sent", models.BooleanField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("RECIPE_SHARING", "Recipe sharing"),
                            ("PASSWORD_RESET", "Password reset"),
                        ],
                        max_length=32,
                    ),
                ),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("breakfast", "breakfast"),
                            ("lunch", "lunch"),
                            ("dinner", "dinner"),
                            ("dessert", "dessert"),
                            ("drink", "drink"),
                            ("appetizer", "appetizer"),
                            ("bakery", "bakery"),
                        ],
                        max_length=32,
                    ),
                ),
                ("content", models.TextField()),
                ("nb_of_people", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default-image.jpg",
                        max_length=1000,
                        null=True,
                        upload_to="images",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        default="default-image.jpg",
                        null=True,
                        upload_to="thumbnails",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("EN", "English"),
                            ("FR", "Français"),
                            ("PL", "Polski"),
                        ],
                        max_length=32,
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "ingredients",
                    models.ManyToManyField(
                        related_name="ingredients",
                        through="app.IngredientQuantity",
                        to="app.ingredient",
                    ),
                ),
                (
                    "is_favorited_by",
                    models.ManyToManyField(
                        related_name="favorites", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "posted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="VoteHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vote",
                    models.CharField(
                        choices=[("UP", "Up"), ("DOWN", "Down")], max_length=16
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.recipe"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ranking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("up", models.IntegerField(default=0)),
                ("down", models.IntegerField(default=0)),
                (
                    "recipe",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ranking",
                        to="app.recipe",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ingredientquantity",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.recipe"
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.recipe"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="AppetizerRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.CreateModel(
            name="BakeryRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.CreateModel(
            name="BreakfastRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.CreateModel(
            name="DessertRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.CreateModel(
            name="DinnerRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.CreateModel(
            name="DrinkRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.CreateModel(
            name="LunchRecipe",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.recipe",),
        ),
        migrations.AddConstraint(
            model_name="votehistory",
            constraint=models.UniqueConstraint(
                fields=("user", "recipe"), name="unique_vote"
            ),
        ),
        migrations.AddConstraint(
            model_name="recipe",
            constraint=models.UniqueConstraint(
                fields=("name", "language"), name="unique_recipe"
            ),
        ),
    ]
