import click

from sqlalchemy_utils import database_exists, create_database

from snakeeyes.app import create_app
from snakeeyes.extensions import db
from snakeeyes.blueprints.user.models import User


app = create_app()
db.app = app


@click.group()
def cli():
    
    pass


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
              help='Create a test db too?')
def init(with_testdb):
    
    db.drop_all()
    db.create_all()

    if with_testdb:
        db_uri = '{0}_test'.format(app.config['SQLALCHEMY_DATABASE_URI'])

        if not database_exists(db_uri):
            create_database(db_uri)

    return None


@click.command()
def seed():
    
    if User.find_by_identity(app.config['SEED_ADMIN_EMAIL']) is not None:
        return None

    params = {
        'role': 'admin',
        'email': app.config['SEED_ADMIN_EMAIL'],
        'password': app.config['SEED_ADMIN_PASSWORD']
    }

    return User(**params).save()


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
              help='Create a test db too?')
@click.pass_context
def reset(ctx, with_testdb):
    
    ctx.invoke(init, with_testdb=with_testdb)
    ctx.invoke(seed)

    return None


cli.add_command(init)
cli.add_command(seed)
cli.add_command(reset)
