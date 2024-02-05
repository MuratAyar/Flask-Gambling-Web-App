from functools import wraps

from flask import flash, redirect
from flask_login import current_user


def anonymous_required(url='/settings'):
    
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_authenticated:
                return redirect(url)

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def role_required(*roles):
    
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role not in roles:
                flash('You do not have permission to do that.', 'error')
                return redirect('/')

            return f(*args, **kwargs)

        return decorated_function

    return decorator
