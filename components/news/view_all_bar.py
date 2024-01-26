from django.template.defaulttags import url
from django_components import component

from comms import models as comms_models


@component.register("news_view_all_bar")
class NewsViewAllBar(component.Component):

    template_name = "news/view_all_bar.html"

    def get_context_data(self, view_all_url, *args, **kwargs):
        return {
            'view_all_url': view_all_url,
            'anchor' : kwargs.pop('anchor', 'left'),
        }
