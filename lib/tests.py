import pytest
from flask import url_for


def assert_status_with_message(status_code=200, response=None, message=None):
    
    assert response.status_code == status_code
    assert message in str(response.data)


class ViewTestMixin(object):
    
    @pytest.fixture(autouse=True)
    def set_common_fixtures(self, session, client):
        self.session = session
        self.client = client

    def login(self, identity='admin@local.host', password='password'):
        
        return login(self.client, identity, password)

    def logout(self):
        
        return logout(self.client)


def login(client, username='', password=''):
    
    user = dict(identity=username, password=password)

    response = client.post(url_for('user.login'), data=user,
                           follow_redirects=True)

    return response


def logout(client):
    
    return client.get(url_for('user.logout'), follow_redirects=True)
