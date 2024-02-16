from django_components import component


@component.register("governance")
class Governance(component.Component):

    template_name = "user/governance.html"

    def get_context_data(self, *args, **kwargs):
        request = kwargs.get('request', None)
        context = super().get_context_data(*args, **kwargs)
        if request:
            context['groups'] = request.press.editorialgroup_set.filter(
                press=request.press,
                journal__isnull=True,
            )

        return context
