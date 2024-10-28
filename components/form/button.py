from django_components import component


@component.register("button")
class Button(component.Component):
    """
    A button intended to work for in-page changes using HTMX.
    """

    template_name = "form/button.html"

    def get_context_data(self, *args, **kwargs):
        foreground = kwargs.get('fg', 'text-white')
        aria_controls = kwargs.get('aria_controls', '')
        defaults = {
            'id': '',
            'name': 'button',
            'value': '',
            'type': 'submit',
            'aria_controls': aria_controls,
            'hx_post': '',
            'hx_target': f'#{ aria_controls }',
            'fg': 'text-white',
            'bg': 'bg-blue',
            'border': 'border-white' if foreground == 'text-white' else 'border-blue',
        }
        context = super().get_context_data(*args, **kwargs)
        context.update(defaults)
        context.update(kwargs)
        return context
