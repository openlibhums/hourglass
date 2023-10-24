from django_components import component


@component.register("team_profile")
class TeamProfile(component.Component):

    template_name = "team/profile.html"

    def get_context_data(self, *args, **kwargs):
        name = kwargs.pop('name', '')
        codename = kwargs.pop('codename', '')
        image_url = kwargs.pop('image_url', '')
        publications = kwargs.pop('publications', True)
        social_links = kwargs.pop('social_links', True)
        context = super().get_context_data(*args, **kwargs)
        context['name'] = name
        context['codename'] = codename
        context['image_url'] = image_url
        context['publications'] = publications
        context['social_links'] = social_links
        return context
