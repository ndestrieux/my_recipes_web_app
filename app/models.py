from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from PIL import Image

from app.enums import CategoryChoice, LanguageChoice, UnitChoice, VoteChoice


class Ingredient(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    category = models.CharField(
        max_length=32,
        choices=[(tag.name, tag.value) for tag in CategoryChoice],
        blank=False,
        null=False,
    )
    ingredients = models.ManyToManyField(
        Ingredient, related_name="ingredients", through="IngredientQuantity"
    )
    content = models.TextField(blank=False, null=False)
    nb_of_people = models.IntegerField(blank=False, null=False)
    image = models.ImageField(
        upload_to="images",
        default="default-image.jpg",
        max_length=1000,
        blank=True,
        null=True,
    )
    thumbnail = models.ImageField(
        upload_to="thumbnails", default="default-image.jpg", blank=True, null=True
    )
    language = models.CharField(
        max_length=32,
        choices=[(tag.name, tag.value) for tag in LanguageChoice],
        blank=False,
        null=False,
    )
    date = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(fields=["name", "language"], name="unique_recipe")
        ]

    def save(self, *args, **kwargs):
        if self.image and self.image.name != "default-image.jpg":
            self.image.name = self.rename_image_file(self.image.name)
            self.thumbnail = self.create_thumbnail(self.image)
        super().save(*args, **kwargs)

    def rename_image_file(self, filename):
        ext = filename.split(".")[-1]
        filename = f"{self.language}_{self.name}.{ext}"
        return filename

    @staticmethod
    def create_thumbnail(image):
        thumb = Image.open(image)
        thumbnail_size = 300
        left = 0
        top = 0
        right = thumbnail_size
        bottom = thumbnail_size
        if thumb.width > thumb.height:
            output_size = (thumb.width, thumbnail_size)
            thumb.thumbnail(output_size, Image.ANTIALIAS)
            left_right_crop = int((thumb.width - thumbnail_size) / 2)
            left = left_right_crop
            right = thumb.width - left_right_crop
            thumb = thumb.crop((left, top, right, bottom))
        elif thumb.width < thumb.height:
            output_size = (thumbnail_size, thumb.height)
            thumb.thumbnail(output_size, Image.ANTIALIAS)
            top_bottom_crop = int((thumb.height - thumbnail_size) / 2)
            top = top_bottom_crop
            bottom = thumb.height - top_bottom_crop
            thumb = thumb.crop((left, top, right, bottom))
        else:
            output_size = (thumbnail_size, thumbnail_size)
            thumb.thumbnail(output_size, Image.ANTIALIAS)
        buffer = BytesIO()
        thumb.save(buffer, format="JPEG")
        thumb = File(buffer, name=image.name)
        return thumb

    def __str__(self):
        return self.name


class BreakfastManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.breakfast.name)


class LunchManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.lunch.name)


class DinnerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.dinner.name)


class DessertManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.dessert.name)


class DrinkManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.drink.name)


class AppetizerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.appetizer.name)


class BakeryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=CategoryChoice.bakery.name)


class BreakfastRecipe(Recipe):
    objects = BreakfastManager()

    class Meta:
        proxy = True


class LunchRecipe(Recipe):
    objects = LunchManager()

    class Meta:
        proxy = True


class DinnerRecipe(Recipe):
    objects = DinnerManager()

    class Meta:
        proxy = True


class DessertRecipe(Recipe):
    objects = DessertManager()

    class Meta:
        proxy = True


class DrinkRecipe(Recipe):
    objects = DrinkManager()

    class Meta:
        proxy = True


class AppetizerRecipe(Recipe):
    objects = AppetizerManager()

    class Meta:
        proxy = True


class BakeryRecipe(Recipe):
    objects = BakeryManager()

    class Meta:
        proxy = True


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    unit = models.CharField(
        max_length=16,
        choices=[(tag.name, tag.value) for tag in UnitChoice],
        blank=True,
        null=True,
    )


class Ranking(models.Model):
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    recipe = models.OneToOneField(
        Recipe,
        blank=False,
        null=False,
        related_name="ranking",
        on_delete=models.CASCADE,
    )

    @property
    def overall(self):
        return self.up - self.down


class VoteHistory(models.Model):
    vote = models.CharField(
        max_length=16,
        choices=[(tag.name, tag.value) for tag in VoteChoice],
        blank=False,
        null=False,
    )
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(
        Recipe, blank=False, null=False, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "recipe"], name="unique_vote")
        ]


class Comment(models.Model):
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(
        Recipe, blank=False, null=False, on_delete=models.CASCADE
    )
