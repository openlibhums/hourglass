from django_components import component
from utils import setting_handler
from utils.logger import get_logger

logger = get_logger(__name__)


@component.register("external_newsletter_signup_form")
class ExternalNewsletterSignupForm(component.Component):

    template_name = "external_newsletter_signup/form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        url = setting_handler.get_setting(
            'general',
            'external_newsletter_signup_url',
            None
        )
        if not url.value:
            logger.warning(
                'External Newsletter Sign-up URL needs setting value.'
            )
        context['external_newsletter_signup_url'] = url.value
        return context
