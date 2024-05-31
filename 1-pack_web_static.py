#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import env, run, sudo, local, cd, put
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        fileName = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {fileName} web_static")
        return fileName
    except:
        return None
