#!/usr/bin/python3
"""
    create a tar archive of the web_static folder
"""

from fabric.api import local, env, lcd
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
