from django.conf import settings

from app.serializers import RecipeSerializer


def get_recipe_pdf_context(instance):
    pdf_context = dict()
    recipe_serializer = RecipeSerializer(instance)
    pdf_context["recipe"] = recipe_serializer.serialize()
    pdf_context["logo_path"] = f".{settings.STATIC_ROOT}/images/version/food-logo.png"
    return pdf_context
