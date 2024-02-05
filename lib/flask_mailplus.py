from flask import render_template

from snakeeyes.extensions import mail


def send_template_message(template=None, ctx=None, *args, **kwargs):
    
    if ctx is None:
        ctx = {}

    if template is not None:
        if 'body' in kwargs:
            raise Exception('You cannot have both a template and body arg.')
        elif 'html' in kwargs:
            raise Exception('You cannot have both a template and body arg.')

        kwargs['body'] = _try_renderer_template(template, **ctx)
        kwargs['html'] = _try_renderer_template(template, ext='html', **ctx)

    mail.send_message(*args, **kwargs)

    return None


def _try_renderer_template(template_path, ext='txt', **kwargs):
    
    try:
        return render_template('{0}.{1}'.format(template_path, ext), **kwargs)
    except IOError:
        pass
