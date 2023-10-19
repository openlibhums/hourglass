from django_components import component


@component.register('supporters_demo_bands_split')
class SupportersDemoBandsSplit(component.Component):

    template_name = 'supporters/demo_bands_split.html'

    def get_context_data(self, *args, **kwargs):
        from plugins.consortial_billing import utils as supporter_utils
        context = super().get_context_data(*args, **kwargs)
        tables = supporter_utils.get_saved_demo_band_data()
        context['higher_supporter_table'] = tables[0]
        context['standard_supporter_table'] = tables[1]
        return context
