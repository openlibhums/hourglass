from django_components import component
from django.forms import widgets


class FormBase(component.Component):

    def get_context_data(self, *args, **kwargs):
        form = kwargs.pop('form', None)
        context = super().get_context_data(*args, **kwargs)

        if not form:
            return context

        for field_name, field in form.fields.items():
            if isinstance(field.widget, widgets.CheckboxInput):
                form.fields[field_name].widget.attrs['class'] = '''
                    border-white bg-white
                '''
            elif isinstance(field.widget, widgets.Select):
                form.fields[field_name].widget.attrs['class'] = '''
                    bg-white w-full
                    max-lg:placeholder:text-md lg:placeholder:text-lg
                    max-lg:text-md lg:text-lg
                    text-black cursor-black placeholder:text-black
                    focus-visible:ring !ring-offset-4
                    !ring-white !ring-offset-blue
                    focus:outline-none focus-visible:outline-none
                    focus:!border-transparent focus-visible:!border-transparent
                    dropdown-arrow
                '''
            elif isinstance(field.widget, widgets.Textarea):
                form.fields[field_name].widget.attrs['class'] = '''
                    bg-white w-full
                    max-lg:placeholder:text-md lg:placeholder:text-lg
                    max-lg:text-md lg:text-lg
                    text-black cursor-black placeholder:text-black
                    focus-visible:ring !ring-offset-4
                    !ring-white !ring-offset-blue
                    focus:outline-none focus-visible:outline-none
                    focus:!border-transparent focus-visible:!border-transparent
                '''
            else:
                form.fields[field_name].widget.attrs['class'] = '''
                    bg-white w-full
                    max-lg:placeholder:text-md lg:placeholder:text-lg
                    max-lg:text-md lg:text-lg
                    text-black cursor-black placeholder:text-black
                    focus-visible:ring !ring-offset-4
                    !ring-white !ring-offset-blue
                    focus:outline-none focus-visible:outline-none
                    focus:!border-transparent focus-visible:!border-transparent
                '''

        context['form'] = form
        return context
