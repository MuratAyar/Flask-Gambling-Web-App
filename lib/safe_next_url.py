try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


from flask import request


def safe_next_url(target):
    
    return urljoin(request.host_url, target)
