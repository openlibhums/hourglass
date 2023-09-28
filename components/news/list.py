from django_components import component
from comms import models


@component.register("news_list")
class NewsList(component.Component):

    template_name = "news/list.html"

    def get_context_data(self, h, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['h'] = h
        return context
