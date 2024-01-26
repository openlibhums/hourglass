from django.db.models import Q
from django_components import component

from comms import models as comms_models


@component.register("news_list")
class NewsList(component.Component):

    template_name = "news/list.html"

    def get_context_data(self, request, *args, **kwargs):
        tag = kwargs.pop('tag', '')
        content_type = kwargs.pop('content_type', '')
        limit = kwargs.pop('limit', None)
        h = kwargs.pop('h', '')
        news_items = kwargs.pop('news_items', [])
        include_tags = kwargs.pop('include_tags', False)
        context = super().get_context_data(*args, **kwargs)

        if not news_items:
            if tag:
                news_items = comms_models.NewsItem.active_objects.filter(
                    content_type=request.model_content_type,
                    object_id=request.site_type.id,
                    tags__text=tag,
                )
            elif content_type and content_type in ['press', 'journal']:
                news_items = comms_models.NewsItem.active_objects.filter(
                    content_type__model=content_type,
                )
            else:
                news_items = comms_models.NewsItem.active_objects.filter()

        if limit:
            news_items = news_items[:limit]

        context = {
            'h': h,
            'news_items': news_items,
            'include_tags': include_tags,
        }

        return context
