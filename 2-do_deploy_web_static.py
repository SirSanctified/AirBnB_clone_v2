#!/usr/bin/python3
"""
    create a tar archive of the web_static folder
"""

from fabric.api import local, env, lcd, run, put
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.25.4.131', '34.239.207.20']


def do_pack():
    """
        Compress the web_static folder
    """
    result = None
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p ./versions")
    with lcd("versions"):
        result = local("sudo tar -czvf web_static_{}.tgz ../web_static/"
                       .format(now))
    if result.succeeded:
        return "./versions/web_static_{}.tgz".format(now)
    else:
        return None


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except Exception:
        return False
