from flask_wtf import Form


class ModelForm(Form):
    
    def __init__(self, obj=None, prefix='', **kwargs):
        Form.__init__(
            self, obj=obj, prefix=prefix, **kwargs
        )
        self._obj = obj


def choices_from_dict(source, prepend_blank=True):
    
    choices = []

    if prepend_blank:
        choices.append(('', 'Please select one...'))

    for key, value in source.items():
        pair = (key, value)
        choices.append(pair)

    return choices


def choices_from_list(source, prepend_blank=True):
    
    choices = []

    if prepend_blank:
        choices.append(('', 'Please select one...'))

    for item in source:
        pair = (item, item)
        choices.append(pair)

    return choices
