from io import BytesIO

from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa

from app.serializers import RecipeSerializer


def render_to_pdf(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    buffer = BytesIO()
    status = pisa.pisaDocument(BytesIO(html.encode("utf-8")), buffer)
    buffer.seek(0)
    pdf_file = buffer.read()
    if not status.err:
        return pdf_file
    return None


def get_recipe_pdf_context(instance):
    pdf_context = dict()
    recipe_serializer = RecipeSerializer(instance)
    pdf_context["recipe"] = recipe_serializer.serialize()
    pdf_context["logo_path"] = settings.STATIC_ROOT + "images/version/food-logo.png"
    return pdf_context
