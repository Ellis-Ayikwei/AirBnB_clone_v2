#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from os.path import exists
from datetime import datetime
from fabric.api import env, run, sudo, local, cd, put
from os.path import isdir
env.hosts = ['100.27.11.38', '107.23.156.4']
import os


def do_pack():
    """
    Generates a tgz archive.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        fileName = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {fileName} web_static")
        print(f"Archive created: {fileName} ({os.path.getsize(fileName)} bytes)")
        return fileName
    except:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        print(f"Uploading archive to server: {archive_path}")
        put(archive_path, '/tmp/')
        print(f"Creating directory for extracted archive: {path}{no_ext}/")
        run(f'mkdir -p {path}{no_ext}/')
        print(f"Extracting archive contents: {archive_path}")
        run(f'tar -xzf /tmp/{file_name} -C {path}{no_ext}/')
        print(f"Removing temporary archive: /tmp/{file_name}")
        run('rm /tmp/{}'.format(file_name))
        print(f"Moving extracted files: {path}{no_ext}/web_static/* to {path}{no_ext}/")
        run(f'mv {path}{no_ext}/web_static/* {path}{no_ext}/')
        print(f"Removing empty directory: {path}{no_ext}/web_static")
        run(f'rm -rf {path}{no_ext}/web_static')
        print(f"Removing old current symlink: /data/web_static/current")
        run('rm -rf /data/web_static/current')
        print(f"Creating new symlink to deployed release: {path}{no_ext}/ -> /data/web_static/current")
        run(f'ln -s {path}{no_ext}/ /data/web_static/current')
        return True
    except:
        return False

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

