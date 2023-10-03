from django_components import component


@component.register("benefits_tile")
class InfographicBenefitsTile(component.Component):

    template_name = "infographic/benefits_tile.html"

    def get_context_data(self, icon_filename, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['icon_filename'] = icon_filename
        return context
