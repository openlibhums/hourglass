from django_components import component


@component.register("link")
class Link(component.Component):

    template_name = "link/link.html"

    def get_context_data(self, *args, **kwargs):
        django_url = kwargs.pop('django_url', '')
        href = kwargs.pop('href', '')
        label = kwargs.pop('label', '')
        base = kwargs.pop('base', '')
        context = super().get_context_data(*args, **kwargs)
        context['django_url'] = django_url
        context['href'] = href
        context['label'] = label
        context['base'] = base
        return context
