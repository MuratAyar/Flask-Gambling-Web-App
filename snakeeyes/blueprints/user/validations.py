from wtforms.validators import ValidationError

from snakeeyes.blueprints.user.models import User


def ensure_identity_exists(form, field):
    
    user = User.find_by_identity(field.data)

    if not user:
        raise ValidationError('Unable to locate account.')


def ensure_existing_password_matches(form, field):
    
    user = User.query.get(form._obj.id)

    if not user.authenticated(password=field.data):
        raise ValidationError('Does not match.')
