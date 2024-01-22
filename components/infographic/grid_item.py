from django_components import component


@component.register("infographic_grid_item")
class InfographicGridItem(component.Component):

    template_name = "infographic/grid_item.html"

    def get_context_data(self, icon, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['icon'] = icon
        return context
