from django_components import component


@component.register("user_group")
class UserGroup(component.Component):

    template_name = "user/group.html"

    def get_context_data(self, *args, **kwargs):
        group = kwargs['group']
        context = super().get_context_data(*args, **kwargs)
        context['group'] = group
        return context
