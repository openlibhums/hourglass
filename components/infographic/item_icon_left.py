from django_components import component


@component.register("infographic_item_icon_left")
class InfographicItemIconLeft(component.Component):

    template_name = "infographic/item_icon_left.html"

    def get_context_data(self, icon, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['icon'] = icon
        return context
