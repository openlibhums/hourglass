from django_components import component


@component.register('supporters_demo_bands')
class SupportersDemoBands(component.Component):

    template_name = 'supporters/demo_bands.html'

    def get_context_data(self, *args, **kwargs):
        from plugins.consortial_billing import utils as supporter_utils
        context = super().get_context_data(*args, **kwargs)
        context['data'] = supporter_utils.get_saved_demo_band_data()

        return context
