from django.db.models import Count
from django_components import component

from comms import models as comms_models


@component.register("news_tag_nav")
class NewsTagNav(component.Component):
    """
    Loads NewsItem lists by tag or by the content type of the
    object (e.g. press, journal).
    """

    template_name = "news/tag_nav.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        all_tags = comms_models.Tag.objects.all().annotate(
            Count('tags')
        ).order_by('-tags__count', 'text')

        context = {
            'all_tags': all_tags,
        }

        return context
