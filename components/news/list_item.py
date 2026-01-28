from django_components import component
from comms import models


@component.register("news_list_item")
class NewsListItem(component.Component):

    template_name = "news/list_item.html"

    def get_context_data(self, item, *args, **kwargs):

        fraction = kwargs.pop('fraction', 'basis-1/3')
        h_level = kwargs.pop('h_level', 'h2')
        include_date = kwargs.pop('include_date', True)
        include_tags = kwargs.pop('include_tags', True)
        if not isinstance(item, models.NewsItem):
            try:
                item = models.NewsItem.objects.get(pk=item)
            except models.NewsItem.DoesNotExist:
                item = None

        context = super().get_context_data(*args, **kwargs)
        context['item'] = item
        context['fraction'] = fraction
        context['h_level'] = h_level
        context['include_date'] = include_date
        context['include_tags'] = include_tags
        return context
