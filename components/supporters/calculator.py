from django_components import component


@component.register('supporters_calculator')
class SupportersCalculator(component.Component):

    template_name = 'supporters/calculator.html'

    def get_context_data(self, *args, **kwargs):
        from plugins.consortial_billing import (
            models as supporter_models,
            forms as supporter_forms
        )
        band_form = kwargs.pop('band_form', supporter_forms.BandForm())
        band = kwargs.pop('band', None)
        request = kwargs.pop('request', None)

        if request and 'calculate' in request.GET:
            band_form = supporter_forms.BandForm(request.GET)
            if band_form.is_valid():
                band = band_form.save(commit=False)
                band_form = supporter_forms.BandForm(
                    instance=band,
                )

        context = super().get_context_data(*args, **kwargs)
        context['currencies'] = supporter_models.Currency.objects.all()
        context['supporters'] = supporter_models.Supporter.objects.filter(
            active=True,
            display=True,
        )
        context['band_form'] = band_form
        context['band'] = band
        return context
