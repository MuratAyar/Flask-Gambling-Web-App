import subprocess

import click


@click.command()
@click.argument('path', default='snakeeyes')
def cli(path):
    
    cmd = 'py.test --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)
