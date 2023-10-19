from django_components import component


@component.register('supporters_demo_table')
class SupportersDemoTable(component.Component):

    template_name = 'supporters/demo_table.html'

    def get_context_data(self, table, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['table'] = table
        return context
