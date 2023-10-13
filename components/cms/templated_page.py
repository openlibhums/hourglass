from django.template.defaultfilters import striptags, truncatewords
from django.template import Template, Context

from django_components import component


@component.register("cms_templated_page")
class CMSTemplatedPage(component.Component):

    template_name = "cms/templated_page.html"

    def get_context_data(self, page, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = page
        page_template = Template(page.content)
        rendered_page = page_template.render(Context(context))
        meta_description = truncatewords(striptags(rendered_page), 25)
        context['meta_description'] = meta_description
        return context
