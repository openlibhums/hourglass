from django.template.utils import ImproperlyConfigured
from django_components import component


@component.register("timeline_section")
class TimelineSection(component.Component):

    def get_template_name(self, context):
        try:
            if context['alternate'] == 'odd':
                return "timeline/section_odd.html"
            elif context['alternate'] == 'even':
                return "timeline/section_even.html"
        except KeyError:
            raise ImproperlyConfigured("Timeline section context must have alternate")

    def get_context_data(self, alternate, *args, **kwargs):
        year = kwargs.pop('year', '')
        context = super().get_context_data(*args, **kwargs)
        context['alternate'] = alternate
        context['year'] = year
        return context
