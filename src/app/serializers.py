from app.models import IngredientQuantity


class RecipeSerializer:
    def __init__(self, instance):
        self.instance = instance

    def serialize(self):
        ingredients = IngredientQuantity.objects.filter(pk=self.instance.pk)
        ingredient_list = []
        for ingredient in ingredients:
            ingredient_list.append(
                {
                    "name": ingredient.ingredient.name,
                    "quantity": ingredient.quantity,
                    "unit": ingredient.unit,
                }
            )
        return {
            "pk": self.instance.pk,
            "name": self.instance.name,
            "category": self.instance.category,
            "ingredients": ingredient_list,
            "content": self.instance.content,
            "nb_of_people": self.instance.nb_of_people,
            "image_path": self.instance.image.path,
            "date": self.instance.date,
            "posted_by": self.instance.posted_by.username,
        }
