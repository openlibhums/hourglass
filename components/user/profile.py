from django_components import component


@component.register("user_profile")
class UserProfile(component.Component):

    template_name = "user/profile.html"

    def get_context_data(self, *args, **kwargs):
        return {
            'user': kwargs.pop('user', ''),
            'staff_groups' : kwargs.pop('staff_groups', ''),
            'governance_groups' : kwargs.pop('governance_groups', ''),
        }
