from django_components import component


@component.register("page_generic")
class PageGeneric(component.Component):

    template_name = "page/generic.html"

    def get_context_data(self, *args, **kwargs):
        return {
            'page': kwargs.pop('page', ''),
            'h1': kwargs.pop('h1', '')
        }
